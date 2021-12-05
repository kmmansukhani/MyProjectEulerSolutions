'''
A number chain is created by continuously adding the square of the digits in a number to form a new number until it has been seen before.

For example,

44 → 32 → 13 → 10 → 1 → 1
85 → 89 → 145 → 42 → 20 → 4 → 16 → 37 → 58 → 89

Therefore any chain that arrives at 1 or 89 will become stuck in an endless loop. What is most amazing is that EVERY starting number will eventually arrive at 1 or 89.

How many starting numbers below ten million will arrive at 89?
'''

def sum_of_digits(n):
    result = 0
    while n > 0:
        result += (n % 10) ** 2
        n //= 10
    return result
def ends_at_89(n):
    if n == 89:
        return True
    if n == 1:
        return False
    return ends_at_89(sum_of_digits(n))
def compute():
    result = 0
    for i in range(1, 10_000_000):
        if ends_at_89(i):
            result += 1
    return result
print(compute())