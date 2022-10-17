#!/usr/bin/env python3
# -*- code: utf-8 -*-
##
## Filename:		boilerplate.py
##
## Description:		boilerplate code for python
##

import logging
from optparse import OptionParser

##
## Create logger with handler
##

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
formatter = logging.Formatter(
            '%(asctime)s : %(name)s : [%(filename)s->%(funcName)s():%(lineno)s] : %(levelname)s : %(message)s',
            '%Y-%m-%d %H:%M:%S')
ch.setFormatter(formatter)
logger.addHandler(ch)

##=======================
##
## Parse Arguments
##
##=======================
def argument_parser():

    parser = OptionParser(usage="%prog [options] files", version="%prog 1.0")
    parser.add_option("-v", "--verbose", action="store_true", dest="verbose", 
        help="verbose mode")

    (options, files) = parser.parse_args()

    return options, files

##=======================
##
## Exampel Class
##
##=======================
class ExampleClass:
    def __init__(self):
        self.logger = logging.getLogger(__name__)

        self.logger.info("ExampleCLass running")

 
##=======================
##
## Main
##
##=======================
if __name__ == '__main__':

    options, files = argument_parser()

    if options.verbose:
        logger.setLevel(logging.DEBUG)
        for handler in logger.handlers:
            if isinstance(handler, type(logging.StreamHandler())):
                handler.setLevel(logging.DEBUG)
                logger.debug('Debug logging enabled')

    EC=ExampleClass()

    for filename in files:
        logger.info(f"Parsing file: {filename}")
##
## This file has not been truncated
##