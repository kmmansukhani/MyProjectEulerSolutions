'''
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
'''

def is_pandigital_product(s):
    nums = ["1","2","3","4","5","6","7","8","9"]
    for i in s:
        if i in nums:
            nums.remove(i)
        else:
            return False
    return len(nums) == 0

def compute(): #for len(str(i) + str(j) + str(i * j)). i * j must be 1 digit x 4 digit or 2 digit x 3 digit
    result = 0
    products = []
    for i in range(10):
        for j in range(1000, 10000):
            s = str(i) + str(j) + str(i * j)
            if is_pandigital_product(s):
                if i * j not in products:
                    products.append(i * j)
                    result += i * j
    for i in range(10, 100):
        for j in range(100,1000):
            s = str(i) + str(j) + str(i * j)
            if is_pandigital_product(s):
                if i * j not in products:
                    products.append(i * j)
                    result += i * j
    return result
print(compute())
