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
- Smart Contracts in directory [contracts](/contracts)


# Approach
Technology that we are going to use:
- Database: The Ethereum’s Testnet Görli blockchain.<!-- - Hosting: IPFS to get free hosting forever in a decentralized platform. -->
- Frontend: React.js with webpack. <!-- - Domain name: Godaddy. Here I could use some decentralized domain service like peername but it’s just faster and easier with godaddy or any other domain registrar. -->
- Contract’s programing language: Solidity 0.8.0, the most common language for developing Smart Contracts.
- Frontend contracts: web3.js to use those contracts in web user interface.
- Frameworks: Brownie to deploy, test and compile smart contracts.<!-- - Development server: Node.js to use the app while developing locally along with testrpc. -->
- Metamask: To use the final application like the end user would.
