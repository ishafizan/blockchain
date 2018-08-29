# 'Hello world' with remix, web3.py, infura.io, rinkeby
### Prerequisites
Linux or Mac is recommended, and you need Python 3.6+. If you are using Windows, either setup a VM or use the Linux Subsystem

- Python 3.7 
- web3.py 4.6.0

### Install web3.py
```
python3 -m venv project_name
source project_name/bin/activate
which python3
which python
pip3 install web3==4.6.0
```
### Install metamask chrome extension
https://metamask.io/

### Get free test eth
- http://rinkeby-faucet.com/
- https://www.rinkeby.io/#faucet
![Alt text](img/Screen%20Shot%202018-08-29%20at%203.38.11%20PM.png)

### Solidity IDE: remix
https://remix.ethereum.org/
- copy Greeter.sol from contracts/ to remix
- monkey around with the interface
- note: easy deploy contract via remix
![Alt text](img/Screen%20Shot%202018-08-29%20at%205.07.10%20PM.png)

### Compiling & deploying the contract via web3.py
- register for free at https://infura.io
- remember to select the rinkeby to copy the url endpoint
![Alt text](img/Screen%20Shot%202018-08-29%20at%203.29.02%20PM.png)

- compiling.py: looks for contract sol file to compile in contract/ folder. A json file will be created under /contract
- note: cache mechanism in place as not to re-compile 
```
cd deploy/
python compile.py
```
![Alt text](img/Screen%20Shot%202018-08-29%20at%205.01.20%20PM.png)

- run deploy.py to deploy the contract to network.
- Note: remix much easier
```
python deploy.py
```

### Interfacing with the contract via web3.py
- take note of the contract address & edit settings.py
![Alt text](img/Screen%20Shot%202018-08-29%20at%205.40.25%20PM.png)

- message_set.py: set message (eg: "hello world") to contract instance
- message_get.py: get current message in contract
- tx_lookup.py: get transaction details 
```
python message_set.py
python message_get.py
python tx_lookup.py
```
![Alt text](img/Screen%20Shot%202018-08-27%20at%206.59.52%20PM.png)
![Alt text](img/Screen%20Shot%202018-08-27%20at%206.59.35%20PM.png)
![Alt text](img/Screen%20Shot%202018-08-29%20at%204.29.37%20PM.png)

### Extra: deploying to Kovan (parity)
- From Metamask, select 'Kovan Test Network'
- optional: get KETH from https://faucet.kovan.network/
- open remix, and deploy contract
![Alt text](img/Screen%20Shot%202018-08-29%20at%208.32.24%20PM.png)
![Alt text](img/Screen%20Shot%202018-08-29%20at%208.31.51%20PM.png)

- edit settings.py accordingly
![Alt text](img/Screen%20Shot%202018-08-29%20at%208.28.46%20PM.png)
- change reference to infura (1 line of code) in message_set.py, message_get.py etc. re-execute. 
Note: opportunity for code re-use -> that's your homework :)
![Alt text](img/Screen%20Shot%202018-08-29%20at%208.45.49%20PM.png)

### References
- https://web3py.readthedocs.io/en/stable/web3.eth.html
- https://web3py.readthedocs.io/en/stable/overview.html#overview-type-conversions

## Author
* **Ishafizan Ishak**


