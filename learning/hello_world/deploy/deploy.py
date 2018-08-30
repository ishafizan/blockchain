# -*- coding: utf-8 -*-
import settings
import util_log
from time import time
import util_gen
import util_web3
from web3 import Web3, HTTPProvider
from web3.middleware import geth_poa_middleware

__author__ = 'Ishafizan'

# --------------------------------------------------
# DEPLOY via WEB3.py
# note: best to deploy to rinkeby network via remix
# --------------------------------------------------
log = util_log.logger()
start = time()
log.info("start: %s" % util_gen.getcurrdt())
log.info("*-" * 40)

# load contract
chain_id = settings.__chain_id__  # 4-rinkeby network
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

# Instantiate contract
try:
    log.info("instantiate and deploy contract...")
    contract = w3.eth.contract(abi=contract_interface['abi'], bytecode=contract_interface["bin"])
except Exception as err:
    raise ValueError(err)

# deploy contract
try:
    wallet_address = util_web3.addr_checksum(log, settings.__wallet_address__, w3)
    log.info("wallet_address: %s" % wallet_address)

    nonce = w3.eth.getTransactionCount(wallet_address)
    txn_dict = {
        'from': wallet_address,
        'gas': 2000000,
        'gasPrice': w3.toWei('21', 'gwei'),
        'nonce': nonce,
        'chainId': chain_id
    }
    # Submit the transaction that deploys the contract
    signed_txn = w3.eth.account.signTransaction(txn_dict, settings.__wallet_private_key__)
    tx_hash = w3.eth.sendRawTransaction(signed_txn.rawTransaction)

    # Wait for the transaction to be mined, and get the transaction receipt
    tx_receipt = w3.eth.waitForTransactionReceipt(tx_hash)
    log.info(tx_receipt)
    log.info("contract_address: %s" % tx_receipt.contractAddress)


except Exception as err:
    raise ValueError(err)

# -- END
end = time()
elapsed_time = end - start
log.info("*-" * 40)
log.info("time taken: %ss" % elapsed_time)
log.info("FINISH")
