#history.py

from colorama import init, Fore

init() #Colorama initialization

class HistoryLog:
    """This is the class that describes itself as a «Calculation History».
       This class stores methods for processing and outputting operations
       performed during the program to file «history.txt»"""

    def __init__(self):
        self.records = []

    def __str__(self): 
        return '\n'.join(f"{i + 1}. {record}" for i, record in enumerate(self.records))

    def _symbol(self, operation):
        return {

            'addition': '+',
            'subtraction': '-',
            'multiplication': '*',
            'division': '/',
            'exponentiation': '^',   

        }.get(operation, '?')

    def add_record(self, operation, x, y=None, result=None):

        if y is None:
            record = f"FACTORIAL: {int(x)}! = {result}"
            self.records.append(record)

        else:
            record = f"{operation.upper()}: {x} {self._symbol(operation)} {y} = {result}"
            self.records.append(record)

    def save_to_file(self, filename="history.txt"):
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                lines = f.readlines()
                start_index = len(lines) + 1

        except FileNotFoundError:
            start_index = 1
            print(Fore.LIGHTRED_EX + f"Error: The file «{filename}» wasn't found.")

        with open(filename, "a", encoding='utf-8') as f:
            for i, record in enumerate(self.records, start=start_index):
                f.write(f"{i}. {record}\n")

    def clear_file(self, filename="history.txt"):
        with open(filename, "w", encoding="utf-8") as f:
            pass
        
        print(Fore.LIGHTMAGENTA_EX + f'The file «{filename}» has been cleared\n')

    