'''
If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?
'''
import math
def maxNumberOfSolution():
    max = 0
    max_p = 0
    for i in range(1001):
        n = numOfSolutions(i)
        if n > max:
            max = n
            max_p = i
    return max_p
def numOfSolutions(p):
    sols = 0
    firstLeg = []
    for a in range(1,p):
        for b in range(1,p):
            if b in firstLeg:
                continue
            c = math.sqrt(a * a + b * b)
            if a + b + c == p:
                firstLeg.append(a)
                sols += 1
    return sols
print(maxNumberOfSolution())
