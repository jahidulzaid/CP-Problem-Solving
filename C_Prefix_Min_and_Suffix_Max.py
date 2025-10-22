# Bismillahir Rahmanir Rahim
# jahidulZaid
# https://codeforces.com/contest/2123/problem/C



def solveit():
    n = int(input())
    a = list(map(int, input().split()))

    pmin = [0] * n
    smax = [0] * n

    pmin[0] = a[0]
    for i in range(1, n):
        pmin[i] = min(pmin[i - 1], a[i])

    smax[-1] = a[-1]
    for i in range(n - 2, -1, -1):
        smax[i] = max(smax[i + 1], a[i])

    winners = set()
    for k in range(n - 1):
        winners.add(min(pmin[k], smax[k + 1]))
        winners.add(max(pmin[k], smax[k + 1]))

    print("".join(['1' if x in winners else '0' for x in a]))

    
for _ in range(int(input())):
    solveit()
