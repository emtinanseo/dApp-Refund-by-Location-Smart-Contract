// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract RefundByLocation {

    enum Status {
        created,
        started,
        compliant,
        noncompliant,
        finished
    }

    event StatusUpdated(uint job_id, address device, Status status);
    event JobCreated(uint job_id);

    address payable Owner public;
    address[] payable Devices public;
    uint[] Jobs public;

    // This function is executed at initialization and sets the owner of the contract
    constructor() payable { 
        Owner = payable(msg.sender); 
    }

    struct Job {
        string name;
        uint job_id;
        uint amount;
        Status status;
        address device;
        //Solidty doesn't have float numbers
        //time duration
        //location limits
        //address
    }

    function create_job() public {
        if(msg.sender == owner) 
    }
}