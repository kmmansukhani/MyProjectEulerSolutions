'''
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.


How many such routes are there through a 20×20 grid?
'''

def fact(n):
  if n == 1:
      return 1
  return n * fact(n-1)
print(int(fact(40)/(fact(20) ** 2)))