from brownie import BasicContract , accounts

def main(): 
    # Fetch the account 
    account = accounts[0] 
    # Deploy contract 
    deploy_contract = BasicContract.deploy({"from":account}) 
    # Print contract address 
    print(f"contract deployed at {deploy_contract}")