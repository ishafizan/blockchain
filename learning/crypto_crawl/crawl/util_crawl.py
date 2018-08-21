# -*- coding: utf-8 -*-
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
import pandas as pd
import json
import pickle
import quandl


# -----------------------------
__author__ = 'Ishafizan'
__data__ = '2018/08/01'


# -----------------------------


# Retrieve Bitcoin Pricing Data
# Pull Kraken Exchange Pricing Data
# Pull Pricing Data From More BTC Exchanges
# Download Trading Data From Poloniex
# -----------------------------

# -----------------------------
# Quandl API KEY
# -----------------------------
def get_api_key(log, token):
    # quandl.ApiConfig.api_key = os.environ[token]
    quandl.ApiConfig.api_key = token
    return quandl.ApiConfig.api_key


# -----------------------------
# Quandl Helper Function
# -----------------------------
def get_quandl_data(log, quandl_id, switch):
    # pickle mode
    if switch == 0:
        # Download and cache Quandl dataseries
        filename = '{}.pkl'.format(quandl_id).replace('/', '-')
        cache_path = "cache/%s" % filename
        log.info("path: %s " % cache_path)
        try:
            f = open(cache_path, 'rb')
            df = pickle.load(f)
            log.info('loaded {} from cache'.format(quandl_id))
        except (OSError, IOError) as e:
            log.info('Downloading {} from Quandl'.format(quandl_id))
            df = quandl.get(quandl_id, returns="pandas")
            df.to_pickle(cache_path)
            log.info('Cached {} at {}'.format(quandl_id, cache_path))
        return df
    # json mode
    elif switch == 1:
        # Download and cache Quandl dataseries
        filename = '{}.json'.format(quandl_id).replace('/', '-')
        cache_path = "cache/%s" % filename
        log.info("path: %s " % cache_path)
        try:
            with open(cache_path) as fd:
                df = json.load(fd)
            # f = open(cache_path, 'w')
            # df = json.loads(f)
            log.info('loaded {} from cache'.format(quandl_id))
        except (OSError, IOError, RuntimeError, ValueError) as e:
            log.info('Downloading {} from Quandl'.format(quandl_id))
            df = quandl.get(quandl_id, returns="json")
            df.to_json(cache_path)
            # df = quandl.get(quandl_id)
            # log.info(df)
            """
            with open(cache_path, 'w') as outfile:
                json.dump(df, outfile)
            """
            log.info('Cached {} at {}'.format(quandl_id, cache_path))
        return df


# -----------------------------
# Poloniex Helper Function
# -----------------------------
def get_crypto_data(poloniex_pair, base_polo_url, start_date, end_date, pediod):
    # Retrieve cryptocurrency data from poloniex
    json_url = base_polo_url.format(poloniex_pair, start_date.timestamp(), end_date.timestamp(), pediod)
    data_df = get_json_data(json_url, poloniex_pair)
    data_df = data_df.set_index('date')
    return data_df


# ----------------------------------------------------------
# download and cache JSON data from a provided URL.
# ----------------------------------------------------------
def get_json_data(json_url, cache_path):
    # Download and cache JSON data, return as a dataframe.
    cache_path = "cache/%s" % cache_path
    try:
        f = open(cache_path, 'rb')
        df = pickle.load(f)
        print('Loaded {} from cache'.format(json_url))
    except (OSError, IOError) as e:
        print('Downloading {}'.format(json_url))
        df = pd.read_json(json_url)
        df.to_pickle(cache_path)
        print('Cached {} at {}'.format(json_url, cache_path))
    return df
