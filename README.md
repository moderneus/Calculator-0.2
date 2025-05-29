# 🧮 Console Calculator with Operation History

This is a console-based calculator written in Python that allows users to perform basic mathematical operations and automatically saves the calculation history to a `history.txt` file. The program supports both binary and unary operations, includes input validation, and provides an `.exe` version for users without a Python environment.

## 📦 Features

- Basic operations:
  - Addition
  - Subtraction
  - Multiplication
  - Division
  - Exponentiation
  - Factorial
- History is automatically saved to `history.txt`
- Option to clear the history file
- Colored console interface (via `colorama`)
- Error handling for invalid inputs and operations
- Pre-built executable available (`.exe`)

## 🖥️ Usage

Run the program and follow the on-screen instructions.  
To select an operation, type the number corresponding to it:

```
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Exponentiation
6. Factorial
```

- To **exit** the program, type: `exit`  
- To **clear** the history, type: `clear`

All operations will be logged in the `history.txt` file in the project directory.

## 📂 File Structure

```bash
.
├── main.py         # Entry point of the program
├── operation.py    # Calculator class with mathematical logic
├── history.py      # Class for handling calculation history
├── history.txt     # (Automatically created) File where results are saved
├── calculator.exe  # (Optional) Compiled executable version
```

## 🔧 Dependencies

- Python 3.x
- [colorama](https://pypi.org/project/colorama/) — used for colored terminal output

You can install the dependency via pip:

```bash
pip install colorama
```

> Note: If you're using the `.exe` version, you don't need to install anything.

## 📌 Implementation Details

- `main.py` handles the user interaction loop and controls program flow.
- `operation.py` defines a `Calculator` class that:
  - Accepts and validates input
  - Performs the operations
  - Sends data to be recorded
- `history.py` contains a `HistoryLog` class that:
  - Formats and stores records
  - Saves records to `history.txt`
  - Can clear the file on user command

## ❗ Error Handling

- Division by zero is caught and properly handled
- Non-numeric input triggers warnings
- Factorial works only for non-negative integers
- Any invalid menu selection is handled gracefully

## 📄 License

This project is open-source and free to use. No license file has been included, but you may use or modify this project as you wish.

## 👤 Author

Created by [moderneus]  
Feel free to modify this README and include your contact or GitHub profile.
