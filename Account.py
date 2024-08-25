""" Create a Account class with methods"""

class Account:
    """Creating an Account class with methods"""
    def __init__(self, balance, interest):
        self.balance = balance
        self.interest = interest

    # This method sets the balance of the account.
    def set_balance(self, balance):
        """Sets the balance for the for the account"""
        self.balance = balance

    # The method sets the interest gained for the account.
    def set_interest(self, interest):
        """Sets the interest gained for the the account"""
        self.interest = interest

    # The method to calculate the interest earned based on the current balance and interest rate
    def calculate_interest(self):
        """Calculates interest earned"""
        return self.balance * (self.interest_rate / 100)

    # The method to update the balance with th eearned interest and return both values
    def update_balance_with_interest(self):
        """Updates balance with the earned interest"""
        interest_earned = self.calculate_interest()
        self.balance += interest_earned
        return self.balance, interest_earned
