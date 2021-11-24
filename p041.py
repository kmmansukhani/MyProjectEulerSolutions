'''
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
'''
import itertools
def is_prime(n):
    if n == 1:
        return False
    i = 2
    while i ** 2 <= n:
        if n % i == 0:
            return False
        i += 1
    return True
def compute(): #n = 4 or 7 because n(n+1)/2 must not be divisible by 3.
    max = 0
    for i in itertools.permutations([1,2,3,4,5,6,7]):
        num = ""
        for j in i:
            num += str(j)
        if int(num) > max and is_prime(int(num)):
            max = int(num)
    return max
print(compute())