'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''



def isDivisibleByAll(n, k):
    for i in range(1,k+1):
        if n % i != 0:
            return False

    return True


def findSmallestNumberDivisbleByAllNumsTillK(k):

    n = 12252240
    while not isDivisibleByAll(n, k):
        n += 1
    return n

print(findSmallestNumberDivisbleByAllNumsTillK(20))