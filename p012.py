
import math
def primeFactors(n):
    exps = {2: 0}
    while n % 2 == 0:
        exps[2] += 1
        n = n / 2
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if i not in exps:
            exps[i] = 0
        while n % i == 0:
            exps[i] += 1
            n /= i
    if n > 2:
        exps[n] = 1
    return exps


def getTriangle():
    for i in range(10000, 100000):
        n = math.ceil(i * (i + 1) / 2)
        arr = primeFactors(n)
        result = 1
        for j in arr:
            if arr[j] != 0:
                result *= (arr[j] + 1)
        if result > 500:
            return n


print(getTriangle())