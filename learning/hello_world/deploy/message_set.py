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
# interact via WEB3.py: set message
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

# call function & set message
try:
    gas_estimate = greeter.functions.setGreeting(set_message).estimateGas()
    log.info("Gas estimate to transact with setVar: {0}".format(gas_estimate))
    log.info("call function & set message: %s" % set_message)
    if gas_estimate > 100000:
        log.warn("gas cost exceeds 100K")
    else:
        wallet_address = util_web3.addr_checksum(log, settings.__wallet_address__, w3)
        nonce = w3.eth.getTransactionCount(wallet_address)
        txn_dict = greeter.functions.setGreeting(set_message).buildTransaction({
            'chainId': chain_id,
            'nonce': nonce,
        })
        # Submit the transaction that sets message
        signed_txn = w3.eth.account.signTransaction(txn_dict, settings.__wallet_private_key__)
        tx_hash = w3.eth.sendRawTransaction(signed_txn.rawTransaction)
        # Wait for transaction to be mined...
        tx_receipt = w3.eth.waitForTransactionReceipt(tx_hash)
        # log.info(tx_receipt)
except Exception as err:
    log.error(err)

# -- END
end = time()
elapsed_time = end - start
log.info("*-" * 40)
log.info("time taken: %ss" % elapsed_time)
log.info("FINISH")
