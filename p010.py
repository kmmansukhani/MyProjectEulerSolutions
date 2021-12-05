
def getKthDigit(n,k):
    count = 0
    digit = n % 10
    while count <= k:
        digit = n % 10
        n //= 10
        count += 1
    return digit
def setKthDigit(n, k, d):
    dig = getKthDigit(n, k)
    n = n - dig * 10 ** k
    return n + d * 10 ** k

assert(setKthDigit(809, 0, 7) == 807)
assert(setKthDigit(809, 1, 7) == 879)
assert(setKthDigit(809, 2, 7) == 709)
assert(setKthDigit(809, 3, 7) == 7809)
assert(setKthDigit(809, 2, 0) == 9)
assert(setKthDigit(0, 4, 7) == 70000)
assert(setKthDigit(0, 2, 0) == 0)
assert(setKthDigit(0, 0, 0) == 0)


