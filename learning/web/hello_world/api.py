# -*- coding: utf-8 -*-
from . import settings
from . import util_web3
from json import dumps, loads
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.serializers.json import DjangoJSONEncoder
from web3 import Web3, HTTPProvider
from web3.middleware import geth_poa_middleware
import binascii

"""
get_transaction_status 
get_transaction_data eg: 0xa1c4e4361b7d618fdca6b4b3c6005531ef272544e56ba0bd6ceee73e97cd4d5b 
blockNumber: 2896459
TxReceipt Status:
"""


# set message
@csrf_exempt
def get_message(request):
    outdata = {}
    status_code = 200
    tx_receipt = False
    chain_id = settings.__chain_id__  # 4-rinkeby network

    try:
        # get web3.py instance
        w3 = Web3(HTTPProvider(settings.__infura_rinkeby__))
        w3.middleware_stack.inject(geth_poa_middleware, layer=0)

        # Create the contract instance with the newly-deployed address
        contract_interface = util_web3.load_contract("", "")
        greeter = w3.eth.contract(address=settings.__contract_address__, abi=contract_interface['abi'])

        message = greeter.functions.greeting().call({'chainId': chain_id})
        tx_receipt = True
    except Exception as err:
        status_code = 418
        message = err.args[1]

    # return response
    outdata.update({"status": status_code, "data": {"text": message, "tx": toJSON(tx_receipt)}})

    if request.method == 'POST':
        callback = request.GET.get('callback')
    else:
        callback = ""
    if callback != "" and callback:
        data = '%s(%s);' % (callback, dumps(outdata, indent=4))
        response = HttpResponse(data, content_type="application/json")
    else:
        response = HttpResponse(
            content=dumps(outdata, cls=DjangoJSONEncoder, indent=4), content_type="application/json"
        )
    return response


# set message
@csrf_exempt
def set_message(request):
    outdata = {}
    status_code = 200
    tx_receipt = False

    if request.method == 'POST':
        message = request.POST.get("message")
    else:
        # message = "Method Not Allowed"
        status_code = 405
        message = request.GET.get("message")

    try:
        # get web3.py instance
        w3 = Web3(HTTPProvider(settings.__infura_rinkeby__))
        w3.middleware_stack.inject(geth_poa_middleware, layer=0)

        # Create the contract instance with the newly-deployed address
        contract_interface = util_web3.load_contract("", "")
        greeter = w3.eth.contract(address=settings.__contract_address__, abi=contract_interface['abi'])

        wallet_address = util_web3.addr_checksum("", settings.__wallet_address__, w3)
        nonce = w3.eth.getTransactionCount(wallet_address)
        chain_id = settings.__chain_id__  # 4-rinkeby network
        txn_dict = greeter.functions.setGreeting(message).buildTransaction({
            'chainId': chain_id,
            'gas': 140000,
            'gasPrice': w3.toWei('21', 'gwei'),
            'nonce': nonce,
        })

        # Submit the transaction that sets message
        signed_txn = w3.eth.account.signTransaction(txn_dict, settings.__wallet_private_key__)
        tx_hash = w3.eth.sendRawTransaction(signed_txn.rawTransaction)

        # Wait for transaction to be mined...
        tx_receipt = w3.eth.waitForTransactionReceipt(tx_hash)
        print(tx_receipt)
        transactionhash = tx_receipt.transactionHash.hex()
        etherscan_tx = "https://rinkeby.etherscan.io/tx/%s," % transactionhash
        etherscan_block = "https://rinkeby.etherscan.io/block/%s," % tx_receipt.blockNumber

    except Exception as err:
        status_code = 418
        message = err.args[1]

    # return response
    # outdata.update({"status": status_code, "data": {"text": message, "tx": toJSON(tx_receipt)}})
    outdata.update({"status": status_code,
                    "data": {"text": message, "tx": {"url": {"block": etherscan_block, "tx": etherscan_tx},
                                                     "transactionHash": transactionhash}}})

    if request.method == 'POST':
        callback = request.GET.get('callback')
    else:
        callback = ""
    if callback != "" and callback:
        data = '%s(%s);' % (callback, dumps(outdata, indent=4))
        response = HttpResponse(data, content_type="application/json")
    else:
        response = HttpResponse(
            content=dumps(outdata, cls=DjangoJSONEncoder, indent=4), content_type="application/json"
        )
    return response


# Looking up transactions
# class to json
def tx_look(request):
    data = {}
    outdata = {}
    status_code = 200
    tx_receipt = False

    if request.method == 'POST':
        txid = request.POST.get("txid")
    else:
        # modify to your own liking. Currently allowing for GET requests
        # message = "Method Not Allowed"
        status_code = 405
        txid = request.GET.get("txid")

    # look up transactions
    # get web3.py instance
    w3 = Web3(HTTPProvider(settings.__infura_rinkeby__))
    w3.middleware_stack.inject(geth_poa_middleware, layer=0)

    # txid = "0xa1c4e4361b7d618fdca6b4b3c6005531ef272544e56ba0bd6ceee73e97cd4d5b"
    data = w3.eth.getTransaction(txid)
    data = util_web3.get_dict(data)

    # return response
    outdata.update({"status": status_code, "data": {"blockNumber": data["blockNumber"]}})

    if request.method == 'POST':
        callback = request.GET.get('callback')
    else:
        callback = ""
    if callback != "" and callback:
        data = '%s(%s);' % (callback, dumps(outdata, indent=4))
        response = HttpResponse(data, content_type="application/json")
    else:
        response = HttpResponse(
            content=dumps(outdata, cls=DjangoJSONEncoder, indent=4), content_type="application/json"
        )
    return response


# -----------------------------------------------------------------------------
# class to json
def toJSON(myobj):
    return dumps(myobj, default=lambda o: o.__dict__,
                 sort_keys=True, indent=4)


@csrf_exempt
def test(request):
    outdata = {"data": "Hello World"}

    if request.method == 'GET':
        callback = request.GET.get('callback')
    else:
        callback = request.POST.get('callback')
    if callback != "" and callback:
        data = '%s(%s);' % (callback, dumps(outdata, indent=4))
        response = HttpResponse(data, content_type="application/json")
    else:
        response = HttpResponse(
            content=dumps(outdata, cls=DjangoJSONEncoder, indent=4), content_type="application/json"
        )
    return response
