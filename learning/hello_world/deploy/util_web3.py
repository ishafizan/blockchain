# -*- coding: utf-8 -*-
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from solc import compile_source
import json

__author__ = 'Ishafizan'


def addr_checksum(log, addr, w3):
    addr = w3.toChecksumAddress(addr)
    # log.info(addr)
    return addr


def get_compiled_contract(log, my_path, filename, sol_file):
    try:
        with open("%s%s" % (my_path, filename)) as fd:
            contract_interface = json.load(fd)
        log.info('loaded {} from cache'.format(filename))
    except (OSError, IOError, RuntimeError, ValueError) as e:
        log.info('Compiling {} from solfile'.format(filename))
        # compile raw contract
        with open("%s%s" % (my_path, sol_file)) as src_file:
            code = src_file.read()
            compiled_sol = compile_source(code)  # Compiled source code
            contract_interface = compiled_sol['<stdin>:Greeter']
        with open("%s%s" % (my_path, filename), 'w') as outfile:
            json.dump(contract_interface, outfile)
        log.info('Cached {} at {}'.format(filename, my_path))
    return contract_interface
