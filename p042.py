'''
The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words, how many are triangle words?
'''
import math
t_inv = lambda t_n: (math.sqrt(1 + 8 * t_n) - 1)/2
def is_triangle_word(s):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    n = 0
    for char in s:
        n += alpha.find(char) + 1
    inv = t_inv(n)
    if inv == math.floor(inv):
        return True
    return False
def compute(arr):
    result = 0
    for i in arr:
        if is_triangle_word(i):
            result += 1
    return result

with open("p042_words.txt") as f:
    contents = f.readlines()
arr = contents[0].split(',')
print(compute(arr))
