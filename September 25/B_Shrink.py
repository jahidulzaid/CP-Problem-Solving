# Bismillahir Rahmanir Rahim
# Jahidul Islam, Green University Of Bangladesh
# @JahidulZaid

import sys

def solve():
    n = int(sys.stdin.readline())
    ans = [1] + list(range(n, 2, -1)) + [2]
    print(*ans)


t = int(sys.stdin.readline())
for _ in range(t):
    solve()

