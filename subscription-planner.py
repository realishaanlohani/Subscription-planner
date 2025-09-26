class BankAccount:
    def __init__(self, initialAm, acctName):
        self.balance = initialAm
        self.name = acctName
        print(f"\nAccount '{self.name}' created. \nBalance = ${self.balance:.2f}")