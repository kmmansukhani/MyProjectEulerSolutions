'''
A googol (10100) is a massive number: one followed by one-hundred zeros; 100100 is almost unimaginably large: one followed by two-hundred zeros. Despite their size, the sum of the digits in each number is only 1.

Considering natural numbers of the form, ab, where a, b < 100, what is the maximum digital sum?
'''
def get_digit_sum(n):
    result = 0
    while n > 0:
        result += n % 10
        n //= 10
    return result
def compute():
    max_sum = 0
    for a in range(1, 100):
        for b in range(1, 100):
            sum = get_digit_sum(a ** b)
            if sum > max_sum:
                max_sum = sum
    return max_sum
print(compute())