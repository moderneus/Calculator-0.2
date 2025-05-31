#operation.py

from history import HistoryLog
from colorama import init, Fore

init() #Colorama initialization

class Calculator():
    """This is the class that stores methods for obtaining numbers
       from a user and methods for mathematical operations with these numbers."""

    def __init__(self):
        self.history_log = HistoryLog()
    
    def save_history(self):
        self.history_log.save_to_file()

    def check_nums(x, y):
        return x is not None and y is not None
    
    def check_num(x):
        return x is not None

    def get_number(self):
        try:
            print(Fore.LIGHTYELLOW_EX + "Type a number:", end=" ")
            x = float(input())

            return x
    
        except ValueError:
            print(Fore.LIGHTRED_EX + "Error: operation are defined only for number.\n")

            return None

    def get_numbers(self):

        try:
            print(Fore.LIGHTYELLOW_EX + "\nType a first number:", end=" ")
            x = float(input())

            print(Fore.LIGHTYELLOW_EX + "Type a second number:", end=" ")
            y = float(input())

            return x, y
    
        except ValueError:
            print(Fore.LIGHTRED_EX + "Error: operation are defined only for numbers.\n")

            return None, None

    def addition(self, x, y):
        if Calculator.check_nums(x, y):
            result = x + y
            print(Fore.LIGHTGREEN_EX + f"Value equals: {result}\n")   

            self.history_log.add_record('addition', x, y, result)
            self.history_log.save_to_file()
    
    def subtraction(self, x, y):
        if Calculator.check_nums(x, y):
            result = x - y
            print(Fore.LIGHTGREEN_EX + f"Value equals: {result}\n")

            self.history_log.add_record('subtraction', x, y, result)
            self.history_log.save_to_file()

    def multiplication(self, x, y):
        if Calculator.check_nums(x, y):
            result = x * y
            print(Fore.LIGHTGREEN_EX + f"Value equals: {result}\n")

            self.history_log.add_record('multiplication', x, y, result)
            self.history_log.save_to_file()

    def division(self, x, y):
        try:
            if Calculator.check_nums(x, y):
                result = x / y
                print(Fore.LIGHTGREEN_EX + f"Value equals: {result}\n")

                self.history_log.add_record('division', x, y, result)
                self.history_log.save_to_file()

        except ZeroDivisionError:
            print(Fore.LIGHTRED_EX + "Error: division by zero is not defined\n")

    def exponentiation(self, x, y):
        if Calculator.check_nums(x, y):
            result = x**y
            print(Fore.LIGHTGREEN_EX + f"Value equals: {result}\n")

            self.history_log.add_record('exponentiation', x, y, result)
            self.history_log.save_to_file()

    def factorial(self, x):
        if Calculator.check_num(x):
            x = int(x)

            if x < 0:
                print(Fore.LIGHTRED_EX + "Error: the factorial is not defined for negative numbers.\n")
                return
            
            if not x.is_integer():
                print(Fore.LIGHTRED_EX + "Error: the factorial is not defined for fractional numbers.\n") 
                return

            def fact(n):

                if n in (0, 1):
                    return 1
            
                else:
                    return n * fact(n - 1)

            result = int(fact(x))
            print(Fore.LIGHTGREEN_EX + f"Value equals: {result}\n")

            self.history_log.add_record(None, x, None, result)
            self.history_log.save_to_file()

    


            
