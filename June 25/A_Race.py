
# jahidulzaid
# https://codeforces.com/contest/2112/problem/0

def solve():
    a, x, y = map(int, input().split())
    found = False
    for b in range(1, 100):
        if b == a:
            continue
        if abs(b - x) < abs(a - x) and abs(b - y) < abs(a - y):
            found = True
            break
    print("YES" if found else "NO")


t = int(input())
for _ in range(t):
    solve()

