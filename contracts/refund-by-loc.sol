// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract RefundByLocation {

    enum Status { created, started, compliant, noncompliant, completed } //job possible statuses

    event StatusUpdated(uint job_id, address device, Status status);
    event JobCreated(uint job_id);

    address payable Owner public;
    address payable[] Devices public;
    uint[] Jobs public;
    uint Amount public;
    uint dT public;

    // This function is executed at initialization and sets the owner of the contract
    constructor() payable { 
        Owner = payable(msg.sender); 
    }

    // A job characteristics
    struct Job {
        string name;
        uint job_id;
        Status status;
        address device;
        //Solidty doesn't have float numbers, we will have to change longitude and latitude values to integers.
        int long_min;
        int long_max;
        int lat_min;
        int lat_max;
        // Dates in Solidity are stored in uint typed variables, we will have to transform datetime to unix timestamp
        uint start_date;
        uint end_date;
    }

    function setAmount (uint _amount) public {
        require(msg.sender == Owner);
        emit AmountSet(_amount);
        Amount = _amount;        
    }


}