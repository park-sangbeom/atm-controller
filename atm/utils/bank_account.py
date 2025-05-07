from typing import Dict, List, Union, Any

""" 
A simple class for handling card operations for bank accounts
"""
class BankAccount:
    def __init__(self) -> None:
        self.accounts: Dict[str, int] = {}
        self.cards: Dict[str, Dict[str, Union[str, List[Dict[str, Any]]]]] = {}
    
    # Register the accounts linked to the card
    def register_card(self, card_number: str, pin: str, accounts: List[Dict[str, Any]]) -> None:
        self.cards[card_number] = {"pin": pin, "accounts": accounts}
    
    # Verify that the entered PIN matches the card PIN
    def check_pin(self, card_number: str, pin: str) -> bool:
        if card_number in self.cards:
            return self.cards[card_number]["pin"] == pin
        return False
    
    # Get the all accounts linked to the card
    def get_accounts(self, card_number: str) -> List[Dict[str, Any]]:
        if card_number in self.cards:
            return self.cards[card_number]["accounts"]
        return []
    
    # Update the balance of the selected bank account 
    def update_account_balance(self, account: Dict[str, Any], amount: int) -> bool:
        account_number = account["account_number"]

        if account_number not in self.accounts:
            self.accounts[account_number] = account["balance"]

        if not isinstance(amount, int):
            return False

        current_balance = self.accounts[account_number]
        new_balance = current_balance + amount

        if new_balance < 0:
            return False

        self.accounts[account_number] = new_balance
        return True