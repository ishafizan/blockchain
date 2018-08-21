# -*- coding: utf-8 -*-
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
import settings
import util_log
import util_gen
import util_crawl
import util_process
import util_viz
import numpy as np
from time import sleep, time
from datetime import datetime
import plotly.graph_objs as go
import plotly.offline as py
import plotly.figure_factory as ff

__author__ = 'Ishafizan'
# --------------------------------------
# inits
base_polo_url = 'https://poloniex.com/public?command=returnChartData&currencyPair={}&start={}&end={}&period={}'
start_date = datetime.strptime('2015-01-01', '%Y-%m-%d')  # get data from the start of 2015
end_date = datetime.now()  # up until today
pediod = 86400  # pull daily data (86,400 seconds per day)
# nine of the top cryptocurrencies -
# Ethereum, Litecoin, Ripple, Ethereum Classic, Stellar, Dash, Siacoin, Monero, and NEM.
# NEO, BCH, IOTA, ZIL, EOS
# altcoins = ['ETH', 'LTC', 'XRP', 'ETC', 'STR', 'DASH', 'SC', 'XMR', 'XEM', 'BCH', 'ETC', 'ZEC','LTC','GNT']
altcoins = ['ETH', 'LTC', 'XRP', 'DASH', 'ZEC', 'LTC', 'GNT']
# altcoins = ['ETH','LTC']

# --------------------------------------
log = util_log.logger()
start = time()
log.info("start: %s" % util_gen.getcurrdt())
log.info("*-" * 40)

# --------------------------------------
# SETUP QUANDL key
# --------------------------------------
apikey = util_crawl.get_api_key(log, settings.TOKEN_QUANDL)
log.info("apikey: %s" % apikey)

# --------------------------------------
# format BCHARTS/{MARKET}{CURRENCY}
# Pull Kraken Exchange Pricing Data
# --------------------------------------
"""
btc_usd_price_kraken = util_crawl.get_quandl_data(log, 'BCHARTS/KRAKENUSD', 0)
btc_usd_price_kraken_json = util_crawl.get_quandl_data(log, 'BCHARTS/KRAKENUSD', 1)
log.info("--------------------------------------")
log.info("\n%s" % btc_usd_price_kraken.head())

# Chart the BTC pricing data
btc_trace = go.Scatter(x=btc_usd_price_kraken.index, y=btc_usd_price_kraken['Weighted Price'])
py.plot([btc_trace])
"""

# Pull pricing data for 3 more BTC exchanges
exchanges = ['COINBASE', 'BITSTAMP', 'ITBIT', 'KRAKEN']
exchange_data = {}
# exchange_data['KRAKEN'] = btc_usd_price_kraken
for exchange in exchanges:
    exchange_code = 'BCHARTS/{}USD'.format(exchange)
    try:
        btc_exchange_df = util_crawl.get_quandl_data(log, exchange_code, 0)
        exchange_data[exchange] = btc_exchange_df
    except ValueError as e:
        log.error(e)
        exit()


# Merge the BTC price dataseries' into a single dataframe
try:
    btc_usd_datasets = util_process.merge_dfs_on_column(list(exchange_data.values()), list(exchange_data.keys()),
                                                        'Weighted Price')
except Exception as e:
    log.error(e)
    exit()

log.info("\n%s\n" % btc_usd_datasets.tail())

# Plot all of the BTC exchange prices
# util_viz.df_scatter(btc_usd_datasets, 'Bitcoin Price (USD) By Exchange')

# Clean and Aggregate the Pricing Data
btc_usd_datasets.replace(0, np.nan, inplace=True)

# Calculate the average BTC price as a new column
btc_usd_datasets['avg_btc_price_usd'] = btc_usd_datasets.mean(axis=1)

# Plot the average BTC price
# btc_trace = go.Scatter(x=btc_usd_datasets.index, y=btc_usd_datasets['avg_btc_price_usd'])
# py.plot([btc_trace])

# ------------------------------------------------------------------
# download exchange data for nine of the top cryptocurrencies
# ------------------------------------------------------------------
log.info("download exchange data for nine of the top cryptocurrencies")
altcoin_data = {}
for altcoin in altcoins:
    coinpair = 'BTC_{}'.format(altcoin)
    filename = '{}.pkl'.format(coinpair)
    cache_path = "cache/%s" % filename
    crypto_price_df = util_crawl.get_crypto_data(coinpair, base_polo_url, start_date, end_date, pediod)
    altcoin_data[altcoin] = crypto_price_df

# preview the last few rows of the Ethereum price
log.info("\n%s\n" % altcoin_data['ETH'].tail())
# Calculate USD Price as a new column in each altcoin dataframe
for altcoin in altcoin_data.keys():
    altcoin_data[altcoin]['price_usd'] = altcoin_data[altcoin]['weightedAverage'] * btc_usd_datasets[
        'avg_btc_price_usd']
# create a combined dataframe of the USD price for each cryptocurrency.
# Merge USD price of each altcoin into single dataframe
try:
    combined_df = util_process.merge_dfs_on_column(list(altcoin_data.values()), list(altcoin_data.keys()), 'price_usd')
except Exception as e:
    log.error(e)
    exit()

# Add BTC price to the dataframe
combined_df['BTC'] = btc_usd_datasets['avg_btc_price_usd']
# Chart all of the altocoin prices
# log.info("solid \"big picture\" view of how the exchange rates for each currency have varied over the past few years")
# using a logarithmic y-axis scale in order to compare all of the currencies on the same plot
# scale='linear')
util_viz.df_scatter(combined_df, 'Cryptocurrency Prices (USD)', seperate_y_axis=False, y_axis_label='Coin Value (USD)',
                    scale='log')
# --------------------------------------
"""
Perform Correlation Analysis Pearson correlation coefficient
https://en.wikipedia.org/wiki/Pearson_correlation_coefficient
Coefficients close to 1 or -1 mean that the series' are strongly correlated or inversely correlated respectively,
and coefficients close to zero mean that the values are not correlated, and fluctuate independently of each other.
"""
# Calculate the pearson correlation coefficients for cryptocurrencies in 2016
combined_df_2016 = combined_df[combined_df.index.year == 2016]
combined_df_2016.pct_change().corr(method='pearson')
combined_df_2017 = combined_df[combined_df.index.year == 2017]
combined_df_2017.pct_change().corr(method='pearson')
combined_df_2018 = combined_df[combined_df.index.year == 2018]
combined_df_2018.pct_change().corr(method='pearson')

util_viz.correlation_heatmap(combined_df_2016.pct_change(), "Cryptocurrency Correlations in 2016", 1)
util_viz.correlation_heatmap(combined_df_2017.pct_change(), "Cryptocurrency Correlations in 2017", 2)
util_viz.correlation_heatmap(combined_df_2018.pct_change(), "Cryptocurrency Correlations in 2018", 3)

# --------------------------------------
# -- END
end = time()
elapsed_time = end - start
log.info("*-" * 40)
log.info("time taken: %ss" % elapsed_time)
log.info("FINISH")
