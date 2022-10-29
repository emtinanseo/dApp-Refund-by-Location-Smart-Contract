pragma solidity 0.4.20;


contract casino {
    address public owner;

    function casino public {
        owner = msg.sender;
    }

    function kill() public {
        if(msg.sender == owner) selfdestruct(owner)
    }
}