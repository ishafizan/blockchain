# -*- coding: utf-8 -*-
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
import pandas as pd

__author__ = 'Ishafizan'

# Merge All Of The Pricing Data Into A Single Dataframe
def merge_dfs_on_column(dataframes, labels, col):
    # Merge a single column of each dataframe into a new combined dataframe
    series_dict = {}
    for index in range(len(dataframes)):
        try:
            series_dict[labels[index]] = dataframes[index][col]
        except Exception as e:
            continue

    return pd.DataFrame(series_dict)
