'''
The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
'''
import math
def is_prime(n):
    if n == 1:
        return False
    i = 2
    while i ** 2 <= n:
        if n % i == 0:
            return False
        i += 1
    return True
def is_truncatable_left_to_right(n): #checks if n is prime
    i = 0
    temp = 0
    while n > 0:
        temp += (n % 10) * 10 ** i
        if not is_prime(temp):
            return False
        i += 1
        n //= 10
    return True
def is_truncatable_right_to_left(n): #does not check if n is prime
    n //= 10
    while n > 0:
        if not is_prime(n):
            return False
        n //= 10
    return True
def compute():
    result = 0
    count = 0
    n = 10
    while count < 11:
        if is_truncatable_right_to_left(n) and is_truncatable_left_to_right(n):
            count += 1
            result += n
        n += 1
    return result
print(compute())