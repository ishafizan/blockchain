# -*- coding: utf-8 -*-
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
import settings
import util_log
import util_gen
from time import sleep, time
from json import dumps
from random import choice

# 2018-06-03
__author__ = 'Ishafizan'

# inits
log = util_log.logger()
start = time()
log.info("start: %s" % util_gen.getcurrdt())
log.info("*" * 40)

# -- END
end = time()
elapsed_time = end - start
ts = util_gen.get_sleep_time(15 * 60, 30 * 60)
log.info("*" * 40)
log.info("time taken: %ss" % elapsed_time)
log.info("FINISHING rest for %ss" % ts)
# sleep(ts)
