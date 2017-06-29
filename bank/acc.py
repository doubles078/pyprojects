#Tutorial for OOP practices
class Account:

    def __init__(self, filepath):
        self.filepath=filepath
        with open(filepath, 'r') as file:
            self.balance=int(file.read())

    def withdraw(self, amount):
        self.balance=self.balance - amount

    def deposit(self, amount):
        self.balance=self.balance + amount

    def commit(self):
        with open(self.filepath, 'w') as file:
            file.write(str(self.balance))

#Showcasing inheritance within OOP
class Checking(Account):
    #This is a class variable and is shared by all instances of a class
    """This is a doc string that helps define what classes are about. Use it like 'checking.__doc___'"""
    type="checking"

    def __init__(self, filepath, fee):
        Account.__init__(self, filepath)
        self.fee=fee

    def transfer(self, amount):
        self.balance=self.balance - amount - self.fee

Checking=Checking("balance.txt", 2)

Checking.transfer(10)
Checking.commit()
print(Checking.balance)
print(Checking.__doc__)