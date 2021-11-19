'''
A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

Easy to solve by hand
10 digits have 10! permutations
If sorted, we start with 0 + perm(1...9), which gives us 9! permutations that start with 0. 9! < 1 million therefore it does not start with 0
1 + perm(0,2,3,4,5,6,7,8,9) => which gives us 9! permutations that start with 1. We are now 2 * 9! permutations deep
2 + perm(0,1,3,4,5,6,7,8,9) => 9! permutations that start with 2. We are now 3 * 9! permutations deep

because 2 * 9! < 1,000,000 < 3 * 9!, we know that the correct answer starts with 2.

The process goes like this:

{0,1,2,3,4,5,6,7,8,9}

find n such that n * 9! is maximized but < 1,000,000. We get n = 2

The digit at the second index is 2.

----------------------------------------

{0,1,3,4,5,6,7,8,9}

find n such that 2 * 9! + n * 8! factorial is maximized but < 1,000,000 (NOT <= 1,000,000). We get n = 6
The digit at the 6th index is 7.

--------------------------------------------------------------------------------------
Repeat until 278391546#

We have only 1 digit left so we will insert it

FINAL ANSWER: 2783915460
'''