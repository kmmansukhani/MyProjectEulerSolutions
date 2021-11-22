'''
The series, 11 + 22 + 33 + ... + 1010 = 10405071317.

Find the last ten digits of the series, 11 + 22 + 33 + ... + 10001000.
'''
def getSum(n):
    sum = 0
    for i in range(1,n+1):
        sum += i ** i
    return sum
def getLastTenDigits(n):
    s = str(n)
    return s[len(s)-10:]
print(getLastTenDigits(getSum(1000)))

