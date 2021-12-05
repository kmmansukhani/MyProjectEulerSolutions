'''
It is possible to show that the square root of two can be expressed as an infinite continued fraction.





By expanding this for the first four iterations, we get:




















The next three expansions are

,

, and

, but the eighth expansion,

, is the first example where the number of digits in the numerator exceeds the number of digits in the denominator.

In the first one-thousand expansions, how many fractions contain a numerator with more digits than the denominator?
'''

from fractions import Fraction
import sys

def calc(n):
    if n == 1:
        return Fraction(1,2)
    return Fraction(1, 2 + calc(n-1))

def is_final_fraction_top_heavy(n):
  to_convert = Fraction(1,1) + calc(n)
  return len(str(to_convert.numerator)) > len(str(to_convert.denominator))

def compute():
  result = 0
  for i in range(1,1001):
    if is_final_fraction_top_heavy(i):
      result += 1
  return result
sys.setrecursionlimit(2000)

print(compute())