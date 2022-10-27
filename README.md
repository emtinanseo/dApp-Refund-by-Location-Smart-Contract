# dApp-Refund-by-Location-Smart-Contract
# Introduction
## Business Need
We have a scenario where a job requires the worker to be in a particular geographic location over a period of time. This could be a security guard or a construction worker, or a similar example. In this scenario, the employer would want a guarantee that an employee is staying in their post for the required duration, while the employees would want a guarantee of payment once they finish the job.

## The Agreement as a Smart Contract
Smart contracts: are digital contracts (simply put: programs) stored on a blockchain that are automatically executed when predetermined terms and conditions are met.
In this case, the smart contract program will receive the GPS location from the employee’s phone, check whether the location satisfies the requirement of being within a specified region. In the case of compliance, it will make out a cryptocurrency payment after a predetermined period of time.
The benefits of using smart contracts: they are fast; execute payments automatically once the conditions are met. They are secure and transparent, encrypted transactions whose records are public on the blockchain. They are immutable; cannot be changed. They save on business costs, as they don’t require a third party to authenticate and handle transactions. 

## Goal
Our goal in this challenge is to produce an Ethereum based dApp. It will have the above mentioned smart contract, with a mobile front-end to be installed in an employee’s phone,   and an employer UI for monitoring.

# Content
- Smart Contracts in directory [contracts](/contracts)
