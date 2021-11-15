'''
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''
import math
def findTrip():
  for a in range(500):
    for b in range(500):
      c = math.sqrt(a ** 2 + b ** 2)
      if a + b + c == 1000:
        return a * b * c
  return -1
print(findTrip())