import pytest
from controller.atm_controller import ATMController

@pytest.fixture
def atm():
    return ATMController()

@pytest.fixture
def test_accounts():
    return [
        {"account_number": "123456789", "balance": 1000},
        {"account_number": "987654321", "balance": 5000}
    ]

@pytest.fixture
def test_card_data():
    return {
        "number": "1234567890123456",
        "pin": "0000",
    }

@pytest.fixture
def test_invalid_card_data():
    return {
        "number":"12345",
        "pin":"1234"
    }

# Card Insertion Test: Valid Case
def test_card_insertion_valid(atm, test_accounts, test_card_data):
    success = atm.insert_card(test_card_data["number"], test_card_data["pin"], test_accounts)
    assert success == True

# Card Insertion Test: Invalid Case
def test_card_insertion_invalid(atm, test_accounts, test_invalid_card_data):
    success = atm.insert_card(test_invalid_card_data["number"], test_invalid_card_data["pin"], test_accounts)
    assert success == False

# PIN Verification Test: Correct PIN
def test_pin_verification_correct(atm, test_accounts, test_card_data):
    atm.insert_card(test_card_data["number"], test_card_data["pin"], test_accounts)
    success = atm.verify_pin(test_card_data["pin"])
    assert success == True

# PIN Verification Test: Incorrect PIN
def test_pin_verification_incorrect(atm, test_accounts, test_card_data):
    atm.insert_card(test_card_data["number"], test_card_data["pin"], test_accounts)
    success = atm.verify_pin("1111")  # Insert the wrong PIN
    assert success == False

# PIN Verification Test: No Card Inserted
def test_pin_verification_without_card(atm, test_card_data):
    success = atm.verify_pin(test_card_data["pin"]) # Skip the card insertion
    assert success == False

# Account Selection Test: Valid Account
def test_account_selection_valid(atm, test_accounts, test_card_data):
    atm.insert_card(test_card_data["number"], test_card_data["pin"], test_accounts)
    success = atm.select_account(0)
    assert success == True

# Account Selection Test: Invalid Account
def test_account_selection_invalid(atm, test_accounts, test_card_data):
    atm.insert_card(test_card_data["number"], test_card_data["pin"], test_accounts)
    success = atm.select_account(5)  # Out of range index
    assert success == False

# Account Selection Test: No Card Inserted
def test_account_selection_without_card(atm):
    success = atm.select_account(0) # Skip the card insertion
    assert success == False

# Balance Check Test: Valid Check
def test_check_balance(atm, test_accounts, test_card_data):
    atm.insert_card(test_card_data["number"], test_card_data["pin"], test_accounts)
    atm.select_account(0)
    balance = atm.check_balance()
    assert balance == 1000

# Balance Check Test: No Account Selected
def test_check_balance_without_account(atm, test_accounts, test_card_data):
    atm.insert_card(test_card_data["number"], test_card_data["pin"], test_accounts)
    balance = atm.check_balance() # Skip the account selection
    assert balance is None

# Deposit Test: Valid Amount
def test_deposit_valid(atm, test_accounts, test_card_data):
    atm.insert_card(test_card_data["number"], test_card_data["pin"], test_accounts)
    atm.select_account(0)
    success = atm.deposit(500)
    assert success == True
    
    # Check if balance is updated
    balance = atm.check_balance()
    assert balance == 1500

# Deposit Test: Negative Amount
def test_deposit_negative_amount(atm, test_accounts, test_card_data):
    atm.insert_card(test_card_data["number"], test_card_data["pin"], test_accounts)
    atm.select_account(0)
    success = atm.deposit(-100)
    assert success == False
    
    # Check if balance remains unchanged
    balance = atm.check_balance()
    assert balance == 1000

# Deposit Test: Non-Integer Amount
def test_deposit_float_amount(atm, test_accounts, test_card_data):
    atm.insert_card(test_card_data["number"], test_card_data["pin"], test_accounts)
    atm.select_account(0)
    success = atm.deposit(100.5)
    assert success == False
    
    # Check if balance remains unchanged
    balance = atm.check_balance()
    assert balance == 1000

# Deposit Test: No Account Selected
def test_deposit_without_account(atm, test_accounts, test_card_data):
    atm.insert_card(test_card_data["number"], test_card_data["pin"], test_accounts)
    success = atm.deposit(500) # Skip the account selection
    assert success == False

# Withdrawal Test: Valid Amount
def test_withdraw_valid(atm, test_accounts, test_card_data):
    atm.insert_card(test_card_data["number"], test_card_data["pin"], test_accounts)
    atm.select_account(0)
    success = atm.withdraw(300)
    assert success == True
    
    # Check if balance is updated
    balance = atm.check_balance()
    assert balance == 700

# Withdrawal Test: Insufficient Balances
def test_withdraw_insufficient_balances(atm, test_accounts, test_card_data):
    atm.insert_card(test_card_data["number"], test_card_data["pin"], test_accounts)
    atm.select_account(0)
    success = atm.withdraw(2000)  # More than account balance
    assert success == False
    
    # Check if balance remains unchanged
    balance = atm.check_balance()
    assert balance == 1000

# Withdrawal Test: Negative Amount
def test_withdraw_negative_amount(atm, test_accounts, test_card_data):
    atm.insert_card(test_card_data["number"], test_card_data["pin"], test_accounts)
    atm.select_account(0)
    success = atm.withdraw(-100)
    assert success == False
    
    # Check if balance remains unchanged
    balance = atm.check_balance()
    assert balance == 1000

# Withdrawal Test: Non-Integer Amount
def test_withdraw_float_amount(atm, test_accounts, test_card_data):
    atm.insert_card(test_card_data["number"], test_card_data["pin"], test_accounts)
    atm.select_account(0)
    success = atm.withdraw(100.5)
    assert success == False
    
    # Check if balance remains unchanged
    balance = atm.check_balance()
    assert balance == 1000

# Withdrawal Test: No Account Selected
def test_withdraw_without_account(atm, test_accounts, test_card_data):
    atm.insert_card(test_card_data["number"], test_card_data["pin"], test_accounts)
    success = atm.withdraw(300) # Skip the account selection
    assert success == False

# End Session Test
def test_end_session(atm, test_accounts, test_card_data):
    atm.insert_card(test_card_data["number"], test_card_data["pin"], test_accounts)
    atm.select_account(0)
    
    success = atm.end_session()
    assert success == True
    
    # Check if session is actually ended
    balance = atm.check_balance()
    assert balance is None

# Full Process Test
def test_full_process(atm, test_accounts, test_card_data):
    # Card insertion
    assert atm.insert_card(test_card_data["number"], test_card_data["pin"], test_accounts) == True
    
    # PIN verification
    assert atm.verify_pin(test_card_data["pin"]) == True
    
    # Account selection
    assert atm.select_account(0) == True
    
    # Balance check
    assert atm.check_balance() == 1000
    
    # Deposit
    assert atm.deposit(500) == True
    assert atm.check_balance() == 1500
    
    # Withdrawal
    assert atm.withdraw(300) == True
    assert atm.check_balance() == 1200
    
    # End session
    assert atm.end_session() == True
    assert atm.check_balance() is None