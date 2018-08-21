# -*- coding: utf-8 -*-
import sys
import getopt
from datetime import datetime
from random import randint
from time import strptime, mktime, sleep

__author__ = 'Ishafizan'


# ---------------------------------------------------
# read vert_id from command line
def get_arg(log):
    try:
        argv = sys.argv[1:]
        opts, args = getopt.getopt(argv, "hg:v", ["help", "vert="])
    except getopt.GetoptError as error:
        log.error(error)
        sys.exit(2)
    try:
        for opt, arg in opts:
            if opt in ("-h", "--help"):
                log.info("help: parse vert_id -v, --vert")
                sys.exit()
            elif opt in ("-v", "--vert"):
                vert = arg
        vert_id = "".join(arg)
        return vert_id
    except Exception as err:
        log.error(err)
        raise ValueError("unable to read vert_id")


# search for key/value in list of dicts
def search_keyval_listdict(strkey, strval, listdict):
    res = (item for item in listdict if item[strkey] == strval.lower()).next()
    return res


# remove dups of dicts in list based on key in dict
# final_match[:] = util_gen.remove_dupes(final_match, "id").values()
def remove_dupes(vals, k):
    seen = {}
    for d in vals:
        v = d[k]
        if v not in seen:
            seen[v] = d
    return seen


# ----------- DATETIMES
# randomise sleep
def get_sleep_time(one, two):
    timer = randint(one, two)
    return timer


# get current time
def getcurrdt():
    dt = datetime.now()
    dt = dt.strftime("%Y-%m-%d %H:%M:%S")
    return dt


# -- facebook specific
def formatdtiso(created_time):
    # FB: 2014-02-11T10:03:34+0000
    time_struct = strptime(created_time, '%Y-%m-%dT%H:%M:%S+0000')
    # time_struct = strptime(created_time, '%Y-%m-%d %H:%M:%S')
    strdate = datetime.fromtimestamp(mktime(time_struct))
    # print strdate
    return strdate


# get current time yyyy-mm-dd
def getcurrdt_yyyymmdd():
    dt = datetime.now()
    dt = dt.strftime("%Y-%m-%d")
    return dt


# string into datetime
def strtodt(mydt):
    mydt = strptime(mydt, "%Y-%m-%d %H:%M:%S")
    return mydt


# operation timerange allowed
def ops_dt(log, currdt):
    # get YYYY-MM-DD
    ymd = getcurrdt_yyyymmdd()
    # change info datetime with start-end datetime
    pme = strtodt("%s %s" % (ymd, "23:59:59"))
    pms = strtodt("%s %s" % (ymd, "10:00:00"))

    if pms <= currdt <= pme:
        log.info("*" * 100)
        log.info("Operation in sleep timerange")
        # sleep for 8 hours
        log.info("Sleep for 8 hours")
        log.info("*" * 100)
        sleep(8 * 60 * 60)

    else:
        log.info("*" * 100)
        log.info("Operation NOT in sleep timerange")
        log.info("*" * 100)


def display_elapsed_time(log, msg, start, end):
    elapsed_time = end - start
    log.info("%s: %ss" % (msg, elapsed_time))
