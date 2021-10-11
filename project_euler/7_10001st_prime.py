'''
10001st prime
problem 7

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?'''

def check_if_prime(num):
    if num > 1:
        for i in range(2,num):
            if (num % i) == 0:
                return False
        return True
check_if_prime(5)

def get_prime_list(num_of_primes):
    primenumber_list = []
    check_num = 2
    while len(primenumber_list)<=num_of_primes:
        if check_if_prime(check_num):
            primenumber_list.append(check_num)
        
        check_num += 1
    return primenumber_list
prime_list = get_prime_list(6)
print(prime_list[5])
prime_list = get_prime_list(10001)
print(prime_list[10000])
# code takes too long! make it more efficient!