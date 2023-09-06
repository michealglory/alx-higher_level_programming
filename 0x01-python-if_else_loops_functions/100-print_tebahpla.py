#!/usr/bin/python3
for letter in range(ord('z'), ord('a') - 1, -1):
    if letter % 2 == 0:
        alpha_diff = 0
    else:
        alpha_diff = 32
    print('{}'.format(chr(letter - alpha_diff)), end='')
