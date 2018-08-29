# 'Hello world' with remix, web3.py, infura.io, rinkeby
### Prerequisites
Linux or Mac is recommended, and you need Python 3.6+. If you are using Windows, either setup a VM or use the Linux Subsystem

Python 3.7, web3.py 4.6.0

### install web3.py
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
- copy Greeter.sol from contracts/
- deploy to rinkeby network

### Interface with web3.py
- register for free at https://infura.io
- remember to select the rinkeby to copy the url endpoint
![Alt text](img/Screen%20Shot%202018-08-29%20at%203.29.02%20PM.png)

- edit settings.py and anter the necessary info
- compiling.py: looks for contract sol file to compile. A json file will be createdundern /contract
- deploy easily via remix to rinkeby network
```
cd deploy/
vi settings.py
python compile.py
```
- message_set.py: set message (eg: "hello world") to contract
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

## Author
* **Ishafizan Ishak**


