'''
<p>Euler discovered the remarkable quadratic formula:</p>
<p class="center">$n^2 + n + 41$</p>
<p>It turns out that the formula will produce 40 primes for the consecutive integer values $0 \le n \le 39$. However, when $n = 40, 40^2 + 40 + 41 = 40(40 + 1) + 41$ is divisible by 41, and certainly when $n = 41, 41^2 + 41 + 41$ is clearly divisible by 41.</p>
<p>The incredible formula $n^2 - 79n + 1601$ was discovered, which produces 80 primes for the consecutive values $0 \le n \le 79$. The product of the coefficients, −79 and 1601, is −126479.</p>
<p>Considering quadratics of the form:</p>
<blockquote>
$n^2 + an + b$, where $|a| &lt; 1000$ and $|b| \le 1000$<br /><br /><div>where $|n|$ is the modulus/absolute value of $n$<br />e.g. $|11| = 11$ and $|-4| = 4$</div>
</blockquote>
<p>Find the product of the coefficients, $a$ and $b$, for the quadratic expression that produces the maximum number of primes for consecutive values of $n$, starting with $n = 0$.</p>
'''


def f(n, a, b):
    return n ** 2 + a * n + b


def isPrime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def findNumOfPrimesProduced(a, b):
    n = 0
    while isPrime(abs(f(n, a, b))):
        n += 1
    return n

def findAB():
    max = 1
    product = 1
    for a in range(-1000, 1001):
        for b in range(-1000, 1001):
            l = findNumOfPrimesProduced(a, b)
            if l > max:
                product = a * b
                max = l
    return product
print(findAB())