#!/usr/bin/python3
if __name__ == "__main__":
    """Handle basic arithmetic operations - addition, subtraction,
    multiplication and division"""
    from calculator_1 import add, sub, mul, div
    import sys

    argv_count = len(sys.argv)
    if argv_count - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    operations = {"+": add, "-": sub, "*": mul, "/": div}
    if sys.argv[2] not in list(operations.keys()):
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[3])
    print("{} {} {} = {}".format(a, sys.argv[2], b,
                                 operations[sys.argv[2]](a, b)))
