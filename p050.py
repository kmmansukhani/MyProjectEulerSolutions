'''
The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?
'''
import sympy

def compute(n):
    max_sum = 0
    longest = 0
    primes = list(sympy.primerange(0,n))
    for i in range(len(primes)):
        for j in range(i+1,len(primes)+1):
            s = sum(primes[i:j])
            if s > n:
                break
            if j - i > longest and s < n and sympy.isprime(s):
                longest = j - i
                max_sum = s

    return max_sum

print(compute(1_000_000))
