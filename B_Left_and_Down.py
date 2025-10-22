# Bismillahir Rahmanir Rahim
# Jahidul Islam, Green University Of Bangladesh
# @JahidulZaid

p = lambda: list(map(int, input().split()))

from math import gcd

t = int(input())
for _ in range(t):
    a, b, k = p()
    g = gcd(a, b)
    dx = a // g
    dy = b // g
    print(1 if dx <= k and dy <= k else 2)
