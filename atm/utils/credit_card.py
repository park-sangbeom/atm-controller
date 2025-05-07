from typing import List, Dict, Any

"""
A simple data model for credit card information 
"""
class CreditCard:
    def __init__(self, card_number: str, card_pin: str, card_accounts: List[Dict[str, Any]]) -> None:
        self.card_number: str = card_number 
        self.card_pin: str = card_pin 
        self.card_accounts: List[Dict[str, Any]] = card_accounts