# -*- coding: utf-8 -*-
import settings
import util_log
from time import time
import util_web3
import util_gen


__author__ = 'Ishafizan'

# ---------------------------
# compile *.sol via WEB3.py
# ---------------------------
log = util_log.logger()
start = time()
log.info("start: %s" % util_gen.getcurrdt())
log.info("*-" * 40)

# settings
filename = settings.__contract_filename__
sol_file = "Greeter.sol"
contract_path = settings.__contract_path__
log.info("path: %s " % contract_path)

contract = util_web3.get_compiled_contract(log, contract_path, filename, sol_file)

# -- END
end = time()
elapsed_time = end - start
log.info("*-" * 40)
log.info("time taken: %ss" % elapsed_time)
log.info("FINISH")
