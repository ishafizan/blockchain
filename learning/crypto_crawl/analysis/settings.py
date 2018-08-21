# -*- coding: utf-8 -*-
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
import sys
__author__ = 'Ishafizan'

import sys
sys.path
sys.path.append('/Library/Python/2.7/site-packages/')
sys.path.append('/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/lib-dynload')

# TOKENS
TOKEN_ACCESS_ID_V6 = "(86, 87)"  # postal dev
TOKEN_ACCESS_ID_V1 = "(86, 87)"  # automotive dev
TOKEN_ACCESS_ID_V16 = "(86, 87)"  # telco dev
TOKEN_ACCESS_ID_V17 = "(86, 87)"  # VVIP dev
TOKEN_ACCESS_ID_V6 = "(86, 87)"  # postal dev
TOKEN_ACCESS_ID_V18 = "(86, 87)"  # politics dev

ERROR_CNT = 5
PAGING_LIMIT = 5
ITEM_FEED_LIMIT = 50

ES_SOURCE = "127.0.0.1"  # "54.169.17.185"  #  "10.10.10.51"  # "183.81.165.246"
ES_TARGET = "127.0.0.1"  # "54.169.17.185"  # "10.10.10.51"  # "183.81.165.246"
ES_SOURCE_INDEX = "fb_2018"  # "temp_percenti_2018"  # "fb_percenti_2017c"
ES_TARGET_INDEX = "fb_2018"  # "transfer_source"

RECONNECT_CNT = 2
REQUEST_TIMEOUT = 10
REC_SIZE = 20

# mysql
mysql_dict_rebana = {"HOST": 'localhost',
                     "PORT": 3306, "USERNAME": "root", "PASSWORD": 'datainsights',
                     "DATABASE": 'rebana'}

mysql_dict_robot = {"HOST": 'localhost',
                    "PORT": 3306, "USERNAME": "root", "PASSWORD": 'datainsights',
                    "DATABASE": 'robot'}
"""
mysql_dict_rebana = {"HOST": 'dashboardrds1.czp0py3xmy0i.ap-southeast-1.rds.amazonaws.com',
                     "PORT": 3306, "USERNAME": "labu", "PASSWORD": 'reson8$%^',
                     "DATABASE": 'rebana'}

mysql_dict_robot = {"HOST": 'dashboardrds1.czp0py3xmy0i.ap-southeast-1.rds.amazonaws.com',
                    "PORT": 3306, "USERNAME": "labi", "PASSWORD": 'orbs$%^',
                    "DATABASE": 'robot'}
"""