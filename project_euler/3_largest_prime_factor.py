'''
Largest prime factor 
Problem 3 

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''
def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n: #the largest prime factor will never be larger than the square root of n
        if n % i:     # same as n % i == 0
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors
print(prime_factors(600851475143))