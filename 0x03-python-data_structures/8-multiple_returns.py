#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence != '':
        first_ch = sentence[0]
    else:
        first_ch = None
    return (len(sentence), first_ch)
