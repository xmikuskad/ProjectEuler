from calendar import weekday
from functools import reduce
from datetime import datetime, timedelta
import math


#   1
#   Problem 1 - Multiples of 3 and 5
#   https://projecteuler.net/problem=1
def is_multiple(num):
    return num % 3 == 0 or num % 5 == 0


def multiples_three_five(num):
    return sum(filter(is_multiple, range(1, num)))


#   2
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


#   3
#   Problem 3 - Largest prime factor
#   https://projecteuler.net/problem=3
def is_divider(diviser, divident):
    return divident % diviser == 0


def is_prime(num):
    for i in range(2, int(math.sqrt(num + 1)) + 1):
        if (num % i) == 0:
            return False
    return True


def get_max_divider(num):
    # vrati pole vsetkych delitelov daneho cisla
    return list(filter(lambda x: is_divider(x, num), range(1, int(math.sqrt(num) + 1))))


def get_max_prime(num):
    return list(filter(is_prime, get_max_divider(num)))[-1:][0]  # posledne cislo v poli


#   3
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


#   4
#   Problem 6 - Sum square difference
#   https://projecteuler.net/problem=6
def get_square_diff(num):
    return sum(range(1, num + 1)) ** 2 - sum(map(lambda x: x ** 2, range(1, num + 1)))


#   5
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


#   6
#   Problem 10 - Summation of primes
#   https://projecteuler.net/problem=10
def primes_gen(num):
    if 2 <= num:
        yield 2
    for iter in range(3, num + 1, 2):
        if all(iter % x != 0 for x in range(3, int(math.sqrt(iter) + 1))):
            yield iter


def primes_sum(num):
    return sum(list(primes_gen(num)));


#   Problem 12 - Highly divisible triangular number
#   https://projecteuler.net/problem=12

#   7
#   Problem 13 - Large sum
#   https://projecteuler.net/problem=13
def to_list(string):
    return map(lambda x: (string[(50 * (x - 1)):])[:50], range(1, 101))


def large_sum(num):
    return int(str(reduce(lambda x, y: int(x) + int(y), list(to_list(str(num)))))[:10])


#   8
#   Problem 16 - Power digit sum
#   https://projecteuler.net/problem=16
def power_digit_sum():
    return reduce(lambda x, y: int(x) + int(y), list(str(2 ** 1000)))


#   9
#   Problem 19 - Counting Sundays
#   https://projecteuler.net/problem=19
def get_dates(start_date, end_date):
    diff = end_date - start_date
    for i in range(diff.days + 1):
        yield start_date + timedelta(days=i)


def counting_sundays():
    return len(list(filter(lambda x: x.day is 1 and x.weekday() is 6,
                           list(get_dates(datetime(1901, 1, 1), datetime(2000, 12, 31))))))


#   10
#   Problem 20 - Factorial digit sum
#   https://projecteuler.net/problem=20
def fac_gen():
    factorial = 1
    i = 1
    while True:
        yield factorial
        factorial *= i
        i += 1


def get_fact(num):
    factorial_gen = fac_gen()
    for i in range(1, num):
        next(factorial_gen)
    return next(factorial_gen)


def fac_dig_sum(num):
    return reduce(lambda x, y: int(x) + int(y), list(str(get_fact(num))))


#   11
#   Problem 40 - Champernowne's constant
#   https://projecteuler.net/problem=40
def champernowne():
    string = reduce(lambda x, y: str(x) + str(y), range(200000))
    return reduce(lambda x, y: x * y,
                  [int(string[1]), int(string[10]), int(string[100]), int(string[1000]), int(string[10000]),
                   int(string[100000]), int(string[1000000])])


#   12
#   Problem 48 - Self powers
#   https://projecteuler.net/problem=48

def self_powers():
    return int(str(reduce(lambda x, y: x + y, list(map(lambda x: pow(x, x), range(1, 1001)))))[-10:])


#   13
#   Problem 52 - Permuted multiples
#   https://projecteuler.net/problem=52
def permutated_checker(num):
    return sorted(str(num)) == sorted(str(num * 2)) == sorted(str(num * 3)) == sorted(str(num * 4)) == sorted(
        str(num * 5)) == sorted(str(num * 6))


def permutated_multiples():
    return list(filter(permutated_checker, range(1, 1000000)))[0]


#   14
#   Problem 56 - Powerful digit sum
#   https://projecteuler.net/problem=56
def get_dig_sum(num):
    return int(reduce(lambda x, y: int(x) + int(y), list(str(num))))


def dig_sum_power(num):
    return sorted(list(map(lambda x: get_dig_sum(num ** x), range(2, 100))), reverse=True)[0]


def powerful_dig_sum():
    return sorted(list(map(lambda x: dig_sum_power(x), range(2, 100))), reverse=True)[0]


#   15
#   Problem 4 - Largest palindrome product
#   https://projecteuler.net/problem=4
def is_palindrome(num):
    return str(num) == str(num)[::-1]


def largest_palindrome_helper(num):
    return max(list(filter(is_palindrome, list(map(lambda x: x * num, range(100, 1000))))), default=0)


def largest_palindrome():
    return max(list(map(largest_palindrome_helper, range(100, 1000))))


#   16
#   Problem 8 - Largest product in a series
#   https://projecteuler.net/problem=8
def get_product(num):
    return reduce(lambda x, y: int(x) * int(y), list(str(num)))


def to_list2(string):
    return map(lambda x: (string[(x):])[:13], range(1000 - 13 + 1))


def largest_product(num):
    return max(list(map(lambda x: get_product(x), list(to_list2(str(num))))))


#   Problem 12 - maybe later finish
def get_divisor_count(num):
    return len(list(filter(lambda x: num % x == 0, range(1, int(math.sqrt(num)) + 1))))


def triangular_gen():
    start = 1;
    iterator = 1
    while True:
        yield start
        iterator += 1
        start += iterator


def divisable_triangular_num():
    gen = triangular_gen()
    return list(filter(lambda x: get_divisor_count(x) > 500, [next(gen) for x in range(80000, 100000)]))[0]


#   17
#   Lattice paths
#   https://projecteuler.net/problem=15
def calculate_coef(num):
    result = 1
    for x in range(1,num+1):
        result = result * (num + x) / x
    return int(result)

#   18
