# -*- coding: utf-8 -*-
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from solc import compile_source
import json
from . import settings

__author__ = 'Ishafizan'


# get dict from attributeDict
def get_dict(myclassdict):
    data = {key: value for key, value in myclassdict.__dict__.items() if
            not key.startswith('__') and not callable(key)}
    return data


def addr_checksum(log, addr, w3):
    addr = w3.toChecksumAddress(addr)
    # log.info(addr)
    return addr


def load_contract(log, sol_file):
    filename = settings.__contract_filename__
    contract_path = settings.__contract_path__
    contract_interface = get_compiled_contract(log, contract_path, filename, sol_file)
    return contract_interface


def get_compiled_contract(log, my_path, filename, sol_file):
    try:
        with open("%s%s" % (my_path, filename)) as fd:
            contract_interface = json.load(fd)
        # log.info('loaded {} from cache'.format(filename))
    except (OSError, IOError, RuntimeError, ValueError) as e:
        # log.info('Compiling {} from solfile'.format(filename))
        # compile raw contract
        with open("%s%s" % (my_path, sol_file)) as src_file:
            code = src_file.read()
            compiled_sol = compile_source(code)  # Compiled source code
            contract_interface = compiled_sol['<stdin>:Greeter']
        with open("%s%s" % (my_path, filename), 'w') as outfile:
            json.dump(contract_interface, outfile)
        # log.info('Cached {} at {}'.format(filename, my_path))
    return contract_interface
