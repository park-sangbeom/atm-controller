from utils.bank_account import BankAccount
from utils.card_checker import CardChecker

class ATMController:
    def __init__(self):
        self.card_checker = None
        self.current_account = None
        self.bank_account = BankAccount()  
    
    # Card insertion and verification 
    def insert_card(self, card_number, card_pin, card_accounts):
        self.card_checker = CardChecker(card_number, card_pin, card_accounts)
        if self.card_checker.is_valid_card():
            self.bank_account.register_card(card_number, card_pin, card_accounts)
            return True
        else: 
            return False
        
    # PIN authentication    
    def verify_pin(self, entered_pin):
        if not self.card_checker:
            return False
        
        if self.bank_account.check_pin(self.card_checker.card_number, entered_pin):
            return True
        else:
            return False
    
    # Bank account selection
    def select_account(self, account_index):
        if not self.card_checker:
            return False
            
        if 0 <= account_index < len(self.card_checker.card_accounts):
            self.current_account = self.card_checker.card_accounts[account_index]
            return True
        return False
    
    # Check the balance of the selected account
    def check_balance(self):
        if not self.current_account:
            return None
        return self.current_account["balance"]
    
    # Make a deposit to the selected account
    def deposit(self, amount):
        if not self.current_account:
            return False
        
        # The deposit must be dollar value which is represented by an Integer
        if not isinstance(amount, int):
            return False
            
        if amount <= 0:
            return False
        
        # Update the balance of the selected account
        self.current_account["balance"] += amount
        self.bank_account.update_account_balance(self.current_account, amount)
        return True

    # Make a withdrawal from the selected account
    def withdraw(self, amount):
        if not self.current_account:
            return False
            
        # The withdrawal must be dollar value which is represented by an Integer
        if not isinstance(amount, int):
            return False
            
        if amount <= 0:
            return False
            
        if amount > self.current_account["balance"]:
            return False 
        
        # Update the balance of the selected account
        self.current_account["balance"] -= amount
        self.bank_account.update_account_balance(self.current_account, -amount)
        return True
    
    # End the ATM Controller
    def end_session(self):
        self.card_checker = None
        self.current_account = None
        return True
