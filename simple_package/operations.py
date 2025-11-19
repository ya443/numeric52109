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
    return a / b


# -------------------------------------------
# Utility helpers
# -------------------------------------------

def _fmt_err(e):
    return f"Error: {e}"

CONSTANTS = {
    'pi': math.pi,
    'e': math.e,
}

def _safe_eval(expr):
    """Safely evaluate simple expressions like pi/2 or (3+4)/2."""
    try:
        return eval(expr, {"__builtins__": None, **CONSTANTS}, {})
    except Exception:
        raise ValueError("invalid expression")

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
# Interface function
# -------------------------------------------

def interface():
    """Fully-featured command-line calculator."""

    ops = {
        # binary operations
        'add': add, 'a': add,
        'subtract': subtract, 'sub': subtract,
        'multiply': multiply, 'mul': multiply,
        'divide': divide, 'div': divide,
        'pow': lambda a, b: a ** b,
        'max': max,
        'min': min,

        # unary operations
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

    # Auto-generated help
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

    last = None

    # Main loop
    while True:
        try:
            line = input("calc> ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nExiting calculator.")
            break

        if not line:
            continue

        parts = line.split()
        cmd = parts[0].lower()

        if cmd in ("exit", "quit"):
            print("Exiting calculator.")
            break

        if cmd in ("help", "h", "?"):
            print(help_text)
            continue

        if cmd not in ops:
            print(f"Unknown command '{cmd}'. Type 'help'.")
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
                print("Wrong number of arguments. Type 'help'.")
        except Exception as e:
            print(_fmt_err(e))


# -------------------------------------------
# Entry point
# -------------------------------------------

if __name__ == "__main__":
    interface()