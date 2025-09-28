# class Book:
#     def __init__(self, title, author, pages):
#         self._title = title
#         self._author = author
#         self.pages = pages
#
#     def __str__(self):
#         return f"{self.author} - {self.title}, {self.pages} stron"
#
#     @property
#     def author(self):
#         return self._author
#     @author.setter
#     def author(self, author):
#         if author.strip():
#             self._author = author.title()
#         else:
#             raise ValueError("Author cannot be empty")
#
#     @property
#     def title(self):
#         return self._title
#     @title.setter
#     def title(self, title):
#         if title.strip():
#             self._title = title.title()
#         else:
#             raise ValueError("Title cannot be empty")
#
# class Ebook(Book):
#     def __init__(self, title, author, pages, file_size):
#         super().__init__(title, author, pages)
#         self.file_size = file_size
#
#     def __str__(self):
#         return super().__str__() + f' {self.file_size} MB'
# kniga = Book("Kniga", "Kniga", 10)
# e_kniga = Ebook("Kniga", "Kniga", 10, 30)
# if __name__ == "__main__":
#     print(kniga)
#     print(e_kniga)
#     kniga.author = ""
#


# class Animal:
#     def __init__(self, name):
#         self.name = name
#
#     def __str__(self):
#         return f'Zwierzę --> {self.name}'
#
# class CanRun:
#     def run(self):
#         return f'{self.name} biegnę'
#
# class CanFly:
#     def fly(self):
#         return f'{self.name} lecę'
#
#
# class Dog(Animal, CanRun):
#     def __init__(self, name):
#         super().__init__(name)
#
# class Bird(Animal, CanRun, CanFly):
#     def __init__(self, name):
#         super().__init__(name)
#
# pies = Dog('Pies')
# ptak = Bird('Ptak')
# print(pies)
# print(ptak)
# print(pies.run())
# print(ptak.run())
# print(ptak.fly())



# class Account:
#     def __init__(self, name, balance):
#         self.name = name
#         self._balance = balance
#
#     def __repr__(self):
#         return f"<Account name='{self.name}' balance='{self._balance}'>"
#     @property
#     def balance(self):
#         return self._balance
#     @balance.setter
#     def balance(self, value):
#         if value < 0:
#             raise ValueError("Balance can't be negative")
#         self.balance = value
#
#     def deposit(self, amount):
#         if amount < 0:
#             raise ValueError("Deposit can't be negative")
#         self.balance += amount
#
#     def withdraw(self, amount):
#         if amount <0:
#             raise(ValueError("Withdraw can't be negative"))
#         if amount > self._balance:
#             raise ValueError("Withdraw can't be greater than balance")
#         self.balance -= amount
#
# class SavingsAccount(Account):
#     def __init__(self, name, balance, interest_rate):
#         super().__init__(name, balance)
#         self.interest_rate = interest_rate
#
#     def add_interest(self, years):
#         self.balance *= (1+self.interest_rate/100)**years
#
#
# konto = Account("Konto", 100)
# print(konto)
# konto.deposit(100)
# print(konto)
# konto.withdraw(100)
# print(konto)
# konto_osz = SavingsAccount("Konto", 100, 5)
# print(konto_osz)
# konto_osz.add_interest(10)
# print(konto_osz)
# konto_osz.withdraw(100)
# print(konto_osz)





