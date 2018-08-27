pragma solidity ^0.4.17;

contract Greeter {
    string public greeting;

    function Greeter(string initialMessage) public {
        greeting = initialMessage;
    }

    function setGreeting(string _greeting) public {
        greeting = _greeting;
    }

}
