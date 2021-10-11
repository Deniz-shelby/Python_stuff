'''
Summation of primes
Problem 10


The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.'''

import math

def sieve_of_atkins(limit):
 #Initial primes
 primes = [2,3]
 sieve = [False]*(limit+1)
 testingLimit = int(math.sqrt(limit))+1
 
 #For loop for generating x, y
 for x in range(testingLimit):
  for y in range(testingLimit):
   
   #n = 4x^2+y^2
   n = 4*int(x**2)+int(y**2)
   if n <= limit and (n%12 ==1 or n%12 ==5):
    sieve[n] = True
   
   #n = 3x^2+y^2
   n = 3*int(x**2)+int(y**2)
   if n<= limit and (n%12 == 7):
    sieve[n] = True
   
   #n = 3x^2-y^2
   n = 3*int(x**2) - int(y**2)
   if n<= limit and x > y and n%12 == 11:
    sieve[n] = True

 #for loop to remove all the multiples of primes
 for i in range(5,testingLimit):
  if sieve[i]:
   index = i**2
   while index < limit:
    sieve[index] = False
    index += i

 #for loop to create prime numbers list
 for i in range(2,len(sieve)):
  if sieve[i]:
   primes.append(i)
 return primes

#Printing the output
print(sum(sieve_of_atkins(2000000)))