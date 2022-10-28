from brownie import BasicContract , accounts

def main(): 
    # Fetch an account from accounts provided by Ganache CLI
    account = accounts[0] 
    # Deploy contract using deploy function of the contractContainer object (BasicContact) 
    deploy_contract = BasicContract.deploy({"from":account}) 
    # Print contract address (deploy_contract is a ProjectContract object) 
    print(f"contract deployed at {deploy_contract}")