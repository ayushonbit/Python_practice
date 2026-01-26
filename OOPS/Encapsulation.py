# Definition: Bundling data (attributes) and methods (functions) that operate on the data into a single unit (class), while restricting direct access to some components.

# Key Concepts:
# Private attributes (using _ or __ naming conventions).

# Getters & Setters (controlled access using @property decorators).


class BankAccount:
    def __init__(self, account_holder, balance=0):
        self._account_holder = account_holder  # Protected attribute
        self.__balance = balance               # Private attribute

    # Getter (access)
    @property
    def balance(self):
        return self.__balance

    # Setter (modify with validation)
    @balance.setter
    def balance(self, amount):
        if amount < 0:
            raise ValueError("Balance cannot be negative!")
        self.__balance = amount

    def deposit(self, amount):
        self.balance += amount  # Uses setter

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient funds!")
        self.balance -= amount

# Usage
account = BankAccount("Alice", 1000)
account.deposit(500)
account.withdraw(200)
print(account.balance)  # Output: 1300
account.balance = -100  # Raises ValueError