'''
The 5-digit number, 16807=75, is also a fifth power. Similarly, the 9-digit number, 134217728=89, is a ninth power.

How many n-digit positive integers exist which are also an nth power?
'''
#NOT SOLVED
import math
def get_num_of_digits(n):
    return math.floor(math.log(n, 10) + 1)
def is_nth_power(i, n):
    return math.isclose(float(int(i ** (1/n))), i ** (1/n), rel_tol=0.0000000001)

def compute():
    count = 0
    for i in range(10, 500_000_000):
        if is_nth_power(i, get_num_of_digits(i)):
            print(i)
            count += 1
    return count
#print(compute())
print(get_num_of_digits(134217728))
print(134217728 ** (1/9))
print(is_nth_power(134217728, get_num_of_digits(134217728)))