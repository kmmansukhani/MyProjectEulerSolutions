'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
'''
def isPrime(n):
    for i in range(2, n):
        if n % i == 0:
            return False

    return True

def getNthPrime(n):
    count = 0
    f = 0
    while count <= n:
        f += 1
        if isPrime(f):
            count += 1
    return f
print(getNthPrime(10001))