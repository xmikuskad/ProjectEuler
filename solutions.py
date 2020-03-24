from functools import reduce
import math


#   Problem 1 - Multiples of 3 and 5
#   https://projecteuler.net/problem=1
def is_multiple(num):
    return num % 3 == 0 or num % 5 == 0


def multiples_three_five(num):
    return sum(filter(is_multiple, range(1, num)))


#   Problem 2 - Even Fibonacci numbers
#   https://projecteuler.net/problem=2
def is_odd(num):
    return not num % 2


def get_fibonacci(max_num):
    fib_array = [1, 2]
    while True:
        index = len(fib_array)
        num = fib_array[index - 1] + fib_array[index - 2]
        if num > max_num:
            return fib_array
        fib_array.insert(index, num)


def find_fibonacci(max_num):
    return sum(filter(is_odd, list(get_fibonacci(max_num))))


#   Problem 3 - Largest prime factor
#   https://projecteuler.net/problem=3
def is_divider(diviser, divident):
    return divident % diviser == 0


def is_prime(num):
    for i in range(2, int(math.sqrt(num+1))+1):
        if (num % i) == 0:
            return False
    return True


def get_max_divider(num):
    # vrati pole vsetkych delitelov daneho cisla
    return list(filter(lambda x: is_divider(x, num), range(1, int(math.sqrt(num) + 1))))


def get_max_prime(num):
    return list(filter(is_prime, get_max_divider(num)))[-1:][0]  # posledne cislo v poli


#   Problem 4 - Largest palindrome product
#   https://projecteuler.net/problem=4

#   Problem 5 - Smallest multiple
#   https://projecteuler.net/problem=5
def is_dividable(iter, num):
    # overi, ci je cislo delitelne vsetkymi cislami od 1 po num napr od 1 do 20
    return len(list(filter(lambda x: is_divider(x, iter), range(1, num + 1)))) == num


def multiple(a, b):
    return a * b


def get_smallest_multiple(num):
    addition = reduce(multiple, filter(is_prime, range(1, num)))  # Vypocita sucin prvocisel, ktore musi cislo obsahovat
    iter = addition
    while True:
        iter += addition
        if is_dividable(iter, num):
            return iter


#   Problem 6 - Sum square difference
#   https://projecteuler.net/problem=6
def get_square_diff(num):
    return sum(range(1, num + 1)) ** 2 - sum(map(lambda x: x ** 2, range(1, num + 1)))


#   Problem 7 - 10001st prime
#   https://projecteuler.net/problem=7
def find_nth_prime(num):
    count = 0
    iter = 1
    while True:
        iter += 1
        if (is_prime(iter)):
            count += 1
            if (count == num):
                return iter
