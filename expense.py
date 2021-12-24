import datetime
import math

class Expense:
    def __init__(self, expense_info: tuple):
        self.__nickname: str = expense_info[0]
        self.__type = expense_info[1]
        self.__amount: float = format(expense_info[2], '.2f')
        self.__due_date = expense_info[3]

    def __str__(self):
        return f"{self.__nickname}\n\tType: {self.__type}\n\tAmount: {self.__amount}\n\tDue Date: {self.__due_date}"

    def __repr__(self):
        return f"<{self.__nickname},{self._type},{self.__amount},{self.__due_date}>"
    
    # Get the value of nickname
    def get_nickname(self):
        return self._nickname
    # Set value of nickname to a new nickname
    def set_nickname(self, new_nickname):
        self._nickname = new_nickname
    # Get the value of type
    def get_type(self):
        return self.__type
    # Set the value of type to a new type
    def set_type(self, new_type):
        self.__type = new_type
    # Get the value of amount
    def get_amount(self):
        return self.__amount
    # Set the value of amount to a new amount
    def set_amount(self, new_amount):
        self.__amount = new_amount
    # Get the value of due_date
    def get_due_date(self):
        return self.__due_date
    # Set the value of due_date to a new due date
    def set_due_date(self, new_due_date):
        self.__due_date = new_due_date
