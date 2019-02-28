# Write a function, persistence, that takes in a positive parameter num and returns its multiplicative persistence,
# which is the number of times you must multiply the digits in num until you reach a single digit.

import operator
from functools import reduce
'''
Example
persistence(39) => 3
Because 3*9 = 27, 2*7 = 14, 1*4=4
and 4 has only one digit.
'''

# My solution
''' IMO it's easiest to create a recursive function that 
multiplies the digits until there is a single digit left
'''


def digit_multiplier(n, count):
    n = str(n)
    if len(n) == 1:
        return count
    else:
        total = reduce((lambda x, y: x * y), map(int, n))
        count += 1
        return digit_multiplier(total, count)


def persistence(n):
    value = digit_multiplier(n, 0)
    return value


# Best solution found on codewars
# We also see that the running time is n
# This is better than my solution because
# 1. This is 1 function


def persistence(n):
    i = 0
    while n >= 10:
        n = reduce(operator.mul, [int(x) for x in str(n)], 1)
        i += 1
    return i
