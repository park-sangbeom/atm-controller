from credit_card import CreditCard

"""
A class that ensures the card number and verifies the PIN
"""
class CardChecker(CreditCard):
    def __init__(self, card_number, card_pin, card_accounts):
        super().__init__(card_number, card_pin, card_accounts)
    
    # Check if card number is exactly 16 digits and contains only numbers
    def is_valid_card(self):
        return len(self.card_number) == 16 and self.card_number.isdigit()
