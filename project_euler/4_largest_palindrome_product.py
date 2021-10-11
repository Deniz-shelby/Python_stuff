'''
Largest palindrome product

Problem 4


A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''

def isPalindrom(num): # check if it is Palindrom 
    num= str(num)
    if num == num[::-1]:
        return True
    else:
        return False

def get_largest_palindrom(digits):
    palindrome_list = []
    for a in range(10**(digits-1),10**digits):
        for b in range(100,1000):
            if isPalindrom(a*b) == True:
                palindrome_list.append(a*b)
    return max(palindrome_list)
    
print(get_largest_palindrom(3))