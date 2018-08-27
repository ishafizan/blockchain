# -*- coding: utf-8 -*-
import sys
import getopt
from datetime import datetime
from random import randint

__author__ = 'Ishafizan'


# ---------------------------------------------------
# read filename from command line
def get_arg(log):
    try:
        argv = sys.argv[1:]
        opts, args = getopt.getopt(argv, "hg:f", ["help", "filename="])
    except getopt.GetoptError as error:
        log.error(error)
        sys.exit(2)
    try:
        for opt, arg in opts:
            if opt in ("-h", "--help"):
                log.info("help: parse filename -f, --filename")
                sys.exit()
            elif opt in ("-f", "--filename"):
                filename = arg
        filename = "".join(arg)
        return filename
    except Exception as err:
        log.error(err)
        raise ValueError("unable to read filename")


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


def display_elapsed_time(log, msg, start, end):
    elapsed_time = end - start
    log.info("%s: %ss" % (msg, elapsed_time))
