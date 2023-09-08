#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys

    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    op = ord(sys.argv[2])
    a = int(sys.argv[1])
    b = int(sys.argv[3])

    if op == 43:
        print("{} + {} = {}".format(a, b, add(a, b)))

    elif op == 45:
        print("{} - {} = {}".format(a, b, sub(a, b)))

    elif op == 42:
        print("{} * {} = {}".format(a, b, mul(a, b)))

    elif op == 47:
        print("{} / {} = {}".format(a, b, div(a, b)))

    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)