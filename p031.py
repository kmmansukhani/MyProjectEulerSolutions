'''
In the United Kingdom the currency is made up of pound (£) and pence (p). There are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).
It is possible to make £2 in the following way:

1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
How many different ways can £2 be made using any number of coins?
'''
def bruteforce():
    count = 0
    for i in range(201): #1 penny
        for j in range(101): #2 penny
            for k in range(41):#5 penny
                for w in range(21): #10 penny
                    for z in range(5): #50 penny
                        for l in range(3): # 100 penny
                            if i + 2 * j + 5 * k + 10 * w + 50 * z + 100 * l >= 200:
                                count += 1
    return count + 1
print(bruteforce())