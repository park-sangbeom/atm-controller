from atm_controller import ATMController

def atm_playground():
    print("Start ATM Simulation Playground")
    # Instance the ATM Controller 
    atm = ATMController()

    # Generate the test data
    accounts = [
        {"account_number": "123456789", "balance": 10000},
        {"account_number": "112233445", "balance": 7000}
    ]
    card_data = {"number": "1234567890123456", "pin": "0000"}
    
    print("\n1. Card Insertion.")
    if atm.insert_card(card_data['number'], card_data['pin'], accounts):
        print("Card successfully inserted.")
        
        print("\n2. PIN Verification.")
        if atm.verify_pin(card_data['pin']):
            print("PIN verified successfully.")

            print("\n3. Bank Account Selection.")
            if atm.select_account(0):  # Select first account
                print(f"Bank account selected: {accounts[0]['account_number']}")
                
                # Check balance
                print("\n4. Check Balance.")
                initial_balance = atm.check_balance()
                print(f"Initial balance: ${initial_balance}")
                
                # Test deposit
                print("\n5. Making a Deposit.")
                if atm.deposit(5000):
                    print(f"Successfully deposited $5000. New balance: ${atm.check_balance()}")
                else:
                    print("Deposit failed.")
                
                # Test withdrawal
                print("\n6. Making a Withdrawal.")
                if atm.withdraw(3000):
                    print(f"Successfully withdrew $3000. New balance: ${atm.check_balance()}")
                else:
                    print("Withdrawal failed.")
                
                # End session
                print("\n7. End Session.")
                if atm.end_session():
                    print("Session ended successfully.")
            else:
                print("Account selection failed.")
        else:
            print("Invalid PIN.")
    else:
        print("Card insertion failed.")

if __name__ == "__main__":
    atm_playground()