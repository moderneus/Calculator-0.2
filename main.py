#This is the main file, which is the «heart» of the program
#main.py

import operation
import sys

from operation import Calculator
from history import HistoryLog
from colorama import init, Fore

init() #Colorama initialization

print(Fore.LIGHTWHITE_EX + "All your mathematical calculations will be saved in the file «history.txt» (!)")

print(Fore.LIGHTWHITE_EX +'''  
If you want to exit the program, type "exit".
If you want to clear the calculation history, type "clear" 
                  '''
+ Fore.LIGHTBLUE_EX +     '''
Type the number of the operation you want to use:
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Exponentiation
6. Factorial
                  ''')

while True:

    math = Calculator()
    history = HistoryLog()

    print(Fore.LIGHTCYAN_EX + "Type here your choice:", end=" ")
    choice = str(input()).strip().lower()

    if choice == '1':
        x, y = math.get_numbers()
        math.addition(x, y)

    elif choice == '2':
        x, y = math.get_numbers()
        math.subtraction(x, y)
        
    elif choice == '3':
        x, y = math.get_numbers()
        math.multiplication(x, y)

    elif choice == '4':
        x, y = math.get_numbers()
        math.division(x, y)

    elif choice == '5':
        x, y = math.get_numbers()
        math.exponentiation(x, y)

    elif choice == '6':
        x = math.get_number()
        math.factorial(x)

    elif choice == "clear":
        history.clear_file()

    elif choice == "exit":
        print(Fore.LIGHTMAGENTA_EX + "The program has finished.")
        sys.exit()
    
    else: 
        print(Fore.LIGHTRED_EX + f"Error: There is no operation under the number «{choice}»\n")

