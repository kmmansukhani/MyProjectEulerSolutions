'''
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: As 1! = 1 and 2! = 2 are not sums they are not included.
'''

def fact(n):
    if n <= 1:
        return 1
    return n * fact(n-1)

def sum_of_digit_facts(n):
    result = 0
    while n > 0:
        result += fact(n % 10)
        n //= 10
    return result
def compute():
    result = 0
    for i in range(3,1000000): #arbitrary upper bound
        if sum_of_digit_facts(i) == i:
            result += i
    return result

print(compute())