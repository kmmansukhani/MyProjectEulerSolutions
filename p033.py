'''
The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
'''
from fractions import Fraction
def getIncorrectAnswer(a,b): #11/21
    a_arr = list(str(a))
    b_arr = list(str(b))
    for i in range(len(a_arr)):
        for j in range(len(b_arr)):
            if i < len(a_arr) and j < len(b_arr) and a_arr[i] == b_arr[j]:
                a_arr.pop(i)
                b_arr.pop(j)
    if a != int(''.join(a_arr)) or b != int(''.join(b_arr)):
        return int(''.join(a_arr))/ int(''.join(b_arr))
    return 1


def getFraction():
    product = 1
    for num in range(11,100):
        for denom in range(num+1, 100):
            if denom % 10 == 0:
                continue
            if getIncorrectAnswer(num,denom) == num/denom:
                product *= (num/denom)
    return Fraction(product).limit_denominator()
print(getFraction())