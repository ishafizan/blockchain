# -*- coding: utf-8 -*-
import settings
import util_log
from time import time
import util_gen
import util_web3
from web3 import Web3, HTTPProvider
from web3.middleware import geth_poa_middleware

__author__ = 'Ishafizan'

# ---------------------------
# interact via WEB3.py: get message
# ---------------------------
log = util_log.logger()
start = time()
log.info("start: %s" % util_gen.getcurrdt())
log.info("*-" * 40)
chain_id = settings.__chain_id__  # 4-rinkeby network
set_message = "Hello World. I did it !"

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

# call function and get current message
log.info("call function and get current message ...")
current_message = greeter.functions.greeting().call({'chainId': chain_id})
log.info(current_message)

# -- END
end = time()
elapsed_time = end - start
log.info("*-" * 40)
log.info("time taken: %ss" % elapsed_time)
log.info("FINISH")
