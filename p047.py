import math
def is_prime(n):
    if n == 1:
        return False
    i = 2
    while i ** 2 <= n:
        if n % i == 0:
            return False
        i += 1
    return True
def get_all_primes_under_n(n):
    arr = []
    for i in range(n+1):
        arr.append(True)
    for i in range(2,math.ceil(math.sqrt(n))+1):
        if arr[i]:
            for j in range(i * i, n + 1, i):
                arr[j] = False
    result = []
    for i in range(2, len(arr)):
        if arr[i]:
            result.append(i)
    return result

def get_prime_factors(n):
  arr = get_all_primes_under_n(n)
  factors = []
  for i in arr:
      if n % i == 0:
          factors.append(i)
  return factors
def compute():
  i = 2
  while True:
      if len(get_prime_factors(i)) == 4 and len(get_prime_factors(i+1)) == 4 and  len(get_prime_factors(i+2)) == 4 and len(get_prime_factors(i+3)) == 4:
          return i
      i += 1
print(compute())