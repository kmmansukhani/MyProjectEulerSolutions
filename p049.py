'''
The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?
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

def tuple_to_int(t):
    return int(''.join(map(str, t)))

def has_two_prime_perms(n):

    res = list(map(int, str(n)))
    for i in set(itertools.permutations(res)):
        inte_i = tuple_to_int(i)
        if inte_i > 1000 and inte_i > n and is_prime(inte_i):
            diff = inte_i - n
            for j in set(itertools.permutations(res)):
                inte_j = tuple_to_int(j)
                if inte_j > 1000 and inte_j == inte_i + diff and is_prime(inte_j):
                    terms = [n, inte_i, inte_j]
                    print(terms)
    return []

def compute():
    for i in range(1_000, 10_000):
        if is_prime(i):
            s = has_two_prime_perms(i)
            if len(s) > 0:
                print(s)
print(compute())
