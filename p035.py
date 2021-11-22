'''
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
'''

def isPrime(n):
    if n == 1:
        return False
    i = 2
    while i**2 <= n:
        if n % i == 0:
            return False
        i += 1
    return True

primes = []
notPrime = []
def isCircularPrime(n):
    digit = len(str(n))
    sci = 10 ** (digit - 1)
    for i in range(digit - 1):
        first = n // sci
        left = (n * 10 + first - (first * sci * 10))
        if not isPrime(left):
            notPrime.append(left)
            return False
        else:
            primes.append(left)
        n = left
    return True
def findCircularPrimesUnderN(n):
    count = 0
    for i in range(2, n):
        if i in notPrime:
            continue
        if i in primes and isCircularPrime(i):
            count += 1
        elif isPrime(i) and isCircularPrime(i):
            count += 1
    return count

print(findCircularPrimesUnderN(1000000))
#takes a bit long. About 10 minutes on my computer. Will try to optimize soon.