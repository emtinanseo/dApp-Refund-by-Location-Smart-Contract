# dApp-Refund-by-Location-Smart-Contract
# Introduction
## Business Need
We have a scenario where a job requires the worker to be in a particular geographic location over a period of time. This could be a security guard or a construction worker, or a similar example. In this scenario, the employer would want a guarantee that an employee is staying in their post for the required duration, while the employees would want a guarantee of payment once they finish the job.

## The Agreement as a Smart Contract
Smart contracts: are programs stored on a blockchain that are automatically executed when predetermined terms and conditions are met.
In this case, the smart contract program will receive the GPS location from the employee’s phone, check whether the location satisfies the requirement of being within a specified region. In the case of compliance, it will make out a cryptocurrency payment after a predetermined period of time.
The benefits of using smart contracts: they are fast; execute payments automatically once the conditions are met. They are secure and transparent, encrypted transactions whose records are public on the blockchain. They are immutable; cannot be changed. They save on business costs, as they don’t require a third party to authenticate and handle transactions. 

## Goal
Our goal in this challenge is to produce an Ethereum based dApp. It will have the above mentioned smart contract, with a mobile front-end to be installed in an employee’s phone, and an employer UI for monitoring.

# Content
- Smart Contract for refund by location dApp is in [contracts/refund-by-loc.sol](/contracts/refund-by-loc.sol)


# Approach
## Technologies
- Database: The Ethereum’s Testnet Görli blockchain.<!-- - Hosting: IPFS to get free hosting forever in a decentralized platform. -->
- Frontend: React.js with webpack. <!-- - Domain name: Godaddy. Here I could use some decentralized domain service like peername but it’s just faster and easier with godaddy or any other domain registrar. -->
- Contract’s programing language: Solidity 0.8.0, the most common language for developing Smart Contracts.
- Frontend contracts: web3.js to use those contracts in web user interface.
- Frameworks: Brownie to deploy, test and compile smart contracts.<!-- - Development server: Node.js to use the app while developing locally along with testrpc. -->
- Metamask: To use the final application like the end user would.

## Smart Contract
### Roles:
- Creator(employer) account, who deploys the smart contract 
- Device accounts

### Flow: 
- An employer signs to deploy the contract. 
- The employer account needs to put a deposit of Ether to create a ‘job’ object.
- The ‘job’ also needs an employee’s name, time duration, GPS readings range. 
- Each ‘job’ is identified by a unique job_id number.
- Each ‘job’ has ‘status’, which can take values of:  ‘created’,  ‘started’, ‘compliant’, ‘noncompliant’ and ‘completed’ . At creation, status will be ‘created’
- A device account signes to accept the ‘job’, its status changes to ‘started’
- A function is activated periodically (after a period T) to update the job status, to receive GPS reading from the device account within dT of time.
  - If no value are received within dT, status is changed to ‘noncompliant’
  - If values are received, they are checked against the set GPS range. If the values are within the required range, status is updated to ‘compliant’, otherwise it is updated to ‘noncompliant’.
- A trigger is set for status of ‘noncompliant’, to terminate the job and send back the deposit to the employer
- A trigger is set for the end of job duration, it updates the status to ‘finished’.
- Once updated to ‘finished’, the payment is made to the device account.


