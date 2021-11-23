'''
The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
'''

def isPalindromeNumber(s):
    for i in range(len(s)):
        if s[i] != s[len(s) - i - 1]:
            return False
    return True
def compute():
    result = 0
    for i in range(1000000):
        if isPalindromeNumber(str(i)) and isPalindromeNumber(bin(i)[2:]):
            result += i
    return result
print(compute())
