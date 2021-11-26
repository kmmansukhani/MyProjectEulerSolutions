'''
It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.

9 = 7 + 2×12
15 = 7 + 2×22
21 = 3 + 2×32
25 = 7 + 2×32
27 = 19 + 2×22
33 = 31 + 2×12

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
'''
import sympy
import math
def compute():
  i = 35
  while has_property(i):
    i += 2
  return i
def has_property(n):
  for i in sympy.primerange(0,n+1):
    if int(math.sqrt((n - i)/2)) == math.sqrt((n-i)/2):
      return True
  return False
print(compute())