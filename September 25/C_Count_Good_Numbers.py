
# Bismillahir Rahmanir Rahim
# Jahidul Islam, Green University Of Bangladesh
# @JahidulZaid

from math import gcd
from itertools import combinations


def count_not_divisible(n):
    primes = [2, 3, 5, 7]
    count = 0
    for i in range(1, len(primes)+1):
        for combo in combinations(primes, i):
            lcm = 1
            for p in combo:
                lcm *= p

            if i % 2 == 1:
                count += n // lcm
            else:
                count -= n // lcm
    return n - count 

t = int(input())
for _ in range(t):
    l, r = map(int, input().split())
    result = count_not_divisible(r) - count_not_divisible(l - 1)
    print(result)
