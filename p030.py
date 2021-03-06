'''
Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

1634 = 14 + 64 + 34 + 44
8208 = 84 + 24 + 04 + 84
9474 = 94 + 44 + 74 + 44
As 1 = 14 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
'''

def works(n, power):
    temp = n
    sum = 0
    while temp > 0:
        sum += (temp % 10) ** power
        temp //= 10
    return n == sum
def findSumOfAllNumsThatWork():
    sum = 0
    for i in range(2, 194980): #Found the bound by using a while True before -- not mathematically.
        b = works(i,5)
        if b:
            sum +=i
    return sum
print(findSumOfAllNumsThatWork())