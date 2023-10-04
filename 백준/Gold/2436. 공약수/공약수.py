import math

def GCD(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a

gcd, lcm = map(int, input().split())

mulAB = gcd * lcm

for A in range(math.ceil(math.sqrt(mulAB)), 0, -1):
    B = mulAB // A
    tempGCD = GCD(A, B)
    if  tempGCD == gcd and A // tempGCD * B == lcm:
        print(A, mulAB // A)
        break