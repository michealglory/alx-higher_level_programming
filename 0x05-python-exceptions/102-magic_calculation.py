#!/usr/bin/python3
def magic_calculation(a, b):
    output = 0
    for item in range(1, 3):
        try:
            if item > a:
                raise Exception('Too far')
            else:
                output += (a ** b) / item
        except Exception:
            output = b + a
            break
    return (output)
