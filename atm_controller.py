from bank_account import BankAccount
from card_checker import CardChecker

class ATMController:
    def __init__(self):
        self.card_checker = None
        self.current_account = None
        self.bank_account = BankAccount()  
    
    # Card insertion and verification 
    def insert_card(self, card_number, card_pin, card_accounts):
        self.card_checker = CardChecker(card_number, card_pin, card_accounts)
        if self.card_checker.is_valid_card():
            print("카드가 유효합니다")
            self.bank_account.register_card(card_number, card_pin, card_accounts)
            return True
        else: 
            print("카드가 유효하지 않습니다")
            return False
        
    # PIN authentication    
    def verify_pin(self, entered_pin):
        if not self.card_checker:
            print("먼저 카드를 삽입해주세요")
            return False
        
        if self.bank_account.check_pin(self.card_checker.card_number, entered_pin):
            print("PIN이 올바릅니다")
            return True
        else:
            print("PIN이 올바르지 않습니다")
            return False
    
    # Bank account selection
    def select_account(self, account_index):
        if not self.card_checker:
            print("먼저 카드를 삽입해주세요")
            return False
            
        if 0 <= account_index < len(self.card_checker.card_accounts):
            self.current_account = self.card_checker.card_accounts[account_index]
            print("계좌가 선택되었습니다")
            return True
        print("유효하지 않은 계좌 선택입니다")
        return False
    
    # Check the balance of the selected account
    def check_balance(self):
        if not self.current_account:
            print("먼저 계좌를 선택해주세요")
            return None
        print("잔액 조회가 성공적으로 처리되었습니다")
        return self.current_account["balance"]
    
    # Make a deposit to the selected account
    def deposit(self, amount):
        if not self.current_account:
            print("먼저 계좌를 선택해주세요")
            return False
        
        # The deposit must be dollar value which is represented by an Integer
        if not isinstance(amount, int):
            return False
            
        if amount <= 0:
            print("유효하지 않은 금액입니다")
            return False
        
        # Update the balance of the selected account
        self.current_account["balance"] += amount
        self.bank_account.update_account_balance(self.current_account, amount)
        print(f"{amount}원이 성공적으로 입금되었습니다")
        return True

    # Make a withdrawal from the selected account
    def withdraw(self, amount):
        if not self.current_account:
            print("먼저 계좌를 선택해주세요")
            return False
            
        # The withdrawal must be dollar value which is represented by an Integer
        if not isinstance(amount, int):
            return False
            
        if amount <= 0:
            print("유효하지 않은 금액입니다")
            return False
            
        if amount > self.current_account["balance"]:
            print("잔액이 부족합니다")
            return False 
        
        # Update the balance of the selected account
        self.current_account["balance"] -= amount
        self.bank_account.update_account_balance(self.current_account, -amount)
        print(f"{amount}원이 성공적으로 출금되었습니다")
        return True
    
    # End the ATM Controller
    def end_session(self):
        self.card_checker = None
        self.current_account = None
        return True
