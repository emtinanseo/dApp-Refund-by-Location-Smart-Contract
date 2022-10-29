from brownie import BasicContract , accounts

def main(): 
    # Fetch an account from local accounts provided by Ganache CLI
    # account = accounts[0] 
    account = accounts.load("eo-goerli-account")
    # Deploy contract using deploy function of the contractContainer object (BasicContact) 
    deploy_contract = BasicContract.deploy({"from":account}) 
    # Print contract address (deploy_contract is a ProjectContract object) 
    print(f"contract deployed at {deploy_contract}")

    # Store a number 
    transaction_receipt = deploy_contract.storeNumber(15, {"from":account}) 
    # Wait for transaction confirmation 
    transaction_receipt.wait(1) # Number (1) means wait for a single new block to be mined before we confirm the transaction finality.

    # To read the data, we can use any of the following codes:
    retrieved_number = deploy_contract.readNumber.call() 
    # or 
    # retrieved_number = deploy_contract.readNumber() # brownie will detect that this is a view function and make a call
    # print the retrieved number
    print(f"Number Retrieved : {retrieved_number}")