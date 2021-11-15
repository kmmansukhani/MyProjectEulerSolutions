'''

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''

def isPalindromeNumber(n):
    s = str(n)
    for i in range(len(s)):
        if s[i] != s[len(s) - i - 1]:
            return False
    return True
def findLargestPal():
    max = 1
    for i in range(100, 1000):
        for j in range(10, 1000):
            if i * j > max and isPalindromeNumber(i * j):
                max = i * j
    return max

print(findLargestPal())