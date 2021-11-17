'''
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
'''



def isAbundantNum(n):
  num = 1
  for i in range(2,n//2 + 1):
    if n % i == 0:
      num += i
  return num > n

def getSumOfAllPossibleNums():
  result = 0
  abundants = []
  for i in range(12,28123):
    if isAbundantNum(i):
      abundants.append(i)
  abundant_sums = set([]) #set so no duplicates
  for i in range(len(abundants)):
    for j in range(i, len(abundants)):
      n = abundants[i] + abundants[j]
      if n <= 28123:
        abundant_sums.add(n)
  for i in range(28124):
    if i not in abundant_sums:
      result += i
  return result
print(getSumOfAllPossibleNums())