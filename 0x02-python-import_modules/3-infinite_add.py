#!/usr/bin/python3
if __name__ == "__main__":
    """Print the addition of all arguments."""
    import sys

    count = len(sys.argv)
    sum_total = 0
    for i in range(count - 1):
        sum_total += int(sys.argv[i + 1])
    print("{}".format(sum_total))
