from functools import reduce


#   Problem 1 - Multiples of 3 and 5
#   https://projecteuler.net/problem=1
def is_multiple(num):
    if num % 3 == 0 or num % 5 == 0:
        return True
    else:
        return False


def multiples_three_five(num):
    return sum(filter(is_multiple, list(range(1, num))))
