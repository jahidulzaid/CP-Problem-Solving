# Bismillahir Rahmanir Rahim
# jahidulZaid
# https://codeforces.com/contest/2114/problem/B


t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    s = input().strip()

    c0 = s.count('0')
    c1 = n - c0
    t_pair = n // 2
    bad_pair = t_pair - k

    if c0 < bad_pair or c1 < bad_pair:
        print("NO")
        continue

    rem0 = c0 - bad_pair
    rem1 = c1 - bad_pair

    if rem0 % 2 != 0 or rem1 % 2 != 0:
        print("NO")
    else:
        print("YES")
