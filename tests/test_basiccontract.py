from brownie import BasicContract, accounts

def test_default_value():
    """
      checks for proper contract deployment by trying to retrieve the default value
    """
    # fetch the account
    account = accounts[0]    
    # deploy contract
    deploy_contract = BasicContract.deploy({"from":account})
    #retrieve default number
    retrieved_number = deploy_contract.readNumber()
    expected_result = 0
    assert retrieved_number == expected_result

def test_stored_value():
    """
    makes sure that our storeNumber function is working properly.
    """
    # fetch the account
    account = accounts[0]
    # deploy contract
    deploy_contract = BasicContract.deploy({"from":account})
    # store a number
    transaction_receipt = deploy_contract.storeNumber(1,{"from":account})
    transaction_receipt.wait(1)
    #retrieve number
    retrieved_number = deploy_contract.readNumber()
    expected_result = 1
    assert retrieved_number == expected_result