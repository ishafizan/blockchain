# -*- coding: utf-8 -*-
import settings
import util_log
import util_gen
import util_web3
from json import dumps
from time import time
from web3 import Web3, HTTPProvider
from web3.middleware import geth_poa_middleware

__author__ = 'Ishafizan'

# ---------------------------
# interact via WEB3.py
# ---------------------------
log = util_log.logger()
start = time()
log.info("start: %s" % util_gen.getcurrdt())
log.info("*-" * 40)
chain_id = settings.__chain_id__  # 4-rinkeby network
txid = "0xa41a0e4f6e84e8aa7ff51d238d3ce5c81530b1401163b60e282b86c81d31b434"

# load contract
filename = settings.__contract_filename__
contract_path = settings.__contract_path__
sol_file = "Greeter.sol"
contract_interface = util_web3.get_compiled_contract(log, contract_path, filename, sol_file)

# get web3.py instance
try:
    log.info("get web3.py instance ...")
    w3 = Web3(HTTPProvider(settings.__infura_rinkeby__))
    # Insert a special middleware in web3.py to handle geth-style proof-of-authority
    w3.middleware_stack.inject(geth_poa_middleware, layer=0)
except Exception as err:
    raise ValueError(err)

# Create the contract instance with the newly-deployed address
try:
    log.info("Create the contract instance with the newly-deployed address ...")
    contract_address = util_web3.addr_checksum(log, settings.__contract_address__, w3)
    log.info("contract_addr: %s" % contract_address)
    greeter = w3.eth.contract(address=settings.__contract_address__, abi=contract_interface['abi'])
except Exception as err:
    log.error(err)

data = w3.eth.getTransaction(txid)
log.info(data)

log.info("to: %s" % data.to)
log.info("hash: %s" % data.hash.hex())
log.info("blockHash: %s" % data.blockHash.hex())
log.info("blockNumber: %s" % data.blockNumber)

# -- END
end = time()
elapsed_time = end - start
log.info("*-" * 40)
log.info("time taken: %ss" % elapsed_time)
log.info("FINISH")
