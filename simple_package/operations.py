###
## simple_package - Module operations.py
## Basic online calculator
###

import math

## Here I have defined four functions for the four
## basic operations. 
##
## 1) You should provide an interface function
##    that will prompt the user for input and
##    call the appropriate function based on the
##    user's input. The interface function should
##    continue to prompt the user for input until
##    the user enters'exit'. 
##
## 2) The interface function should also handle
##    any exceptions that might be thrown by the
##    basic operations functions. If an exception 
##    is thrown,the interface function should print 
##    an error message and continue to prompt the 
##    user for input.
##
## 3) Add other "operations" to the calculator, that
##    involve complicated operations (e.g., 
##    trigonometric functions, logarithms, etc.).
##

# -------------------------------------------
# Section 1: Basic operations
# -------------------------------------------

def add(a, b):
    """Add two numbers."""
    return a + b

def subtract(a, b):
    """Subtract one number from another."""
    return a - b

def multiply(a, b):
    """Multiply two numbers."""
    return a * b

def divide(a, b):
    """Divide one number by another."""
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b


# ---------------------------------------------------
# Section 2: Definition of utility helper functions
# ---------------------------------------------------

# turns an expection into a formatted error string
def _fmt_err(e):
    return f"Error: {e}"

# defines common mathematical constants
CONSTANTS = {
    'pi': math.pi,
    'e': math.e,
}

# making use of the eval function to evaluate simple expressions
# but disabling all other built-ins, so users can only access functions we have defined
def _safe_eval(expr):
    """Safely evaluate simple expressions like pi/2 or (3+4)/2."""
    try:
        return eval(expr, {"__builtins__": None, **CONSTANTS}, {})
    except Exception:
        raise ValueError("invalid expression")

# allows user to access the last result, handles exceptions, if any
def _parse_number(s, last):
    """Convert input string to a number or constant."""
    s = s.lower()

    if s == 'last':
        if last is None:
            raise ValueError("no previous result available")
        return last

    if s in CONSTANTS:
        return CONSTANTS[s]

    # Try float
    try:
        return float(s)
    except ValueError:
        pass

    # Try expression
    return _safe_eval(s)


# -------------------------------------------
# Section 3: Interface function
# -------------------------------------------

def interface():
    """Fully-featured command-line calculator."""

    ops = {
        # mapping text commands to binary operations
        'add': add,
        'subtract': subtract, 
        'multiply': multiply, 
        'divide': divide, 
        'pow': lambda a, b: a ** b,
        'max': max,
        'min': min,

        # mapping text commands to unary operations
        'sin': lambda x: math.sin(x),
        'cos': lambda x: math.cos(x),
        'tan': lambda x: math.tan(x),
        'log': lambda x: math.log(x),
        'log10': lambda x: math.log10(x),
        'sqrt': lambda x: math.sqrt(x),
        'exp': lambda x: math.exp(x),
        'abs': lambda x: abs(x),
        'round': lambda x: round(x),
    }

    # scans the ops dictonary to generate help text
    help_text = "Available commands:\n\nBinary (x op y):\n"
    unary_ops, binary_ops = [], []

    for name, fn in ops.items():
        try:
            if fn.__code__.co_argcount == 1:
                unary_ops.append(name)
            else:
                binary_ops.append(name)
        except:
            binary_ops.append(name)

    for op in sorted(binary_ops):
        help_text += f"  {op}\n"

    help_text += "\nUnary (op x):\n"
    for op in sorted(unary_ops):
        help_text += f"  {op}\n"

    help_text += (
        "\nOther commands:\n"
        "  help - show help\n"
        "  exit - quit\n"
        "\nSpecial values:\n"
        "  pi, e, last, or expressions like 3/4 or pi/2\n"
    )

    print(help_text)
    
    # we start with no last result
    last = None
    print("\nHello! 👋 Welcome to the Simple Calculator.")
    print("Type a command below, or type 'help' to see all available operations.\n")

    # We begin the main loop
    while True:
        try:
            line = input("Type your command here → ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\n\nGoodbye! Thanks for using the calculator.")
            break

        if not line:
            continue

        parts = line.split()
        cmd = parts[0].lower()

        if cmd in ("exit", "quit"):
            print("\n\nGoodbye! Thanks for using the calculator.")
            break

        if cmd in ("help", "h", "?"):
            print(help_text)
            continue

        if cmd not in ops:
            print(f"Unfortunately you have entered an unknown command '{cmd}'. Please type 'help', so we can try to assist you!.")
            continue

        func = ops[cmd]

        # Unary operations
        try:
            if len(parts) == 2:
                x = _parse_number(parts[1], last)
                result = func(x)
                print(result)
                last = result
                continue

            # Binary operations
            elif len(parts) == 3:
                a = _parse_number(parts[1], last)
                b = _parse_number(parts[2], last)
                result = func(a, b)
                print(result)
                last = result
                continue

            else:
                print("Unfortunately you have entered an inncorrect number of arguments. Please type 'help', so we can try to assist you!")
        except Exception as e:
            print(_fmt_err(e))


# -------------------------------------------
# Section 4: Script entry point
# -------------------------------------------


# If this file is run directly (e.g. "python operations.py"),
# start the calculator interface.
if __name__ == "__main__":
    interface()