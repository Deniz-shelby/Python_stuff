'''
Smallest multiple

Problem 5

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

'''
smallest_number = 2520
n = 10
def divide_by_all(num):
    for i in range(2,21):
        if num % i != 0:
            return False
        return True
    
from functools import reduce

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

print(reduce(lambda a, b: a * b / gcd(a, b), range(1, 21)))