'''
Comparing two numbers written in index form like 211 and 37 is not difficult, as any calculator would confirm that 211 = 2048 < 37 = 2187.

However, confirming that 632382518061 > 519432525806 would be much more difficult, as both numbers contain over three million digits.

Using base_exp.txt (right click and 'Save Link/Target As...'), a 22K text file containing one thousand lines with a base/exponent pair on each line, determine which line number has the greatest numerical value.

NOTE: The first two lines in the file represent the numbers in the example given above.
'''
import math
with open("p099_base_exp.txt") as f:
    contents = f.read()

arr = []
for i in contents.split('\n'):
    arr.append(i.split(','))

def compare(a, b, max):
    return b > math.log(max, a)

def compute():
    max = 1
    line = 0
    for i in range(len(arr)):
        a = int(arr[i][0])
        b= int(arr[i][1])
        if compare(a,b,max):
            max = a ** b
            line = i
    return line + 1
print(compute())
