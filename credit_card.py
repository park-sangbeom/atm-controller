"""
A simple data model for credit card information 
"""
class CreditCard:
    def __init__(self, card_number, card_pin, card_accounts):
        self.card_number = card_number 
        self.card_pin = card_pin 
        self.card_accounts = card_accounts 
    