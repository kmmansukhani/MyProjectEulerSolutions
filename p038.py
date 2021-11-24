'''
Take the number 192 and multiply it by each of 1, 2, and 3:

192 × 1 = 192
192 × 2 = 384
192 × 3 = 576
By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?
'''

def is_pandigital_product(s):
    nums = ["1","2","3","4","5","6","7","8","9"]
    for i in s:
        if i in nums:
            nums.remove(i)
        else:
            return False
    return len(nums) == 0

def compute(): #range of concatenated products must be i and (1,2,..,j) where i is a maximum four digit number and j is a maximum 1 digit number
    max = 123456789
    for i in range(1,10000):
        for j in range(2, 10):
            s = ""
            for k in range(1, j):
                s += str(i * k)
            if is_pandigital_product(s) and int(s) > max:
                max = int(s)
    return max

print(compute())

