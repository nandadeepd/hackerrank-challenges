#!/bin/python3

import sys

# havent covered all cases - no time :( 

def isValid(s):
    # Complete this function
    dictionary = dict()
    occ = 1
    for c in s:
        if c not in dictionary:
            dictionary[c] = 0
        else:
            dictionary[c] += 1
    val = max(dictionary, key=dictionary.get)
    uniformVal = dictionary [val]
    if all(value == uniformVal for value in dictionary.values()):
        return "YES"
    else:
        return "NO"
    return dictionary

s = input().strip()
result = isValid(s)
print(result)
