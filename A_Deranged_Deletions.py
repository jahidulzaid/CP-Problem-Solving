# Bismillahir Rahmanir Rahim
# jahidulZaid
# https://codeforces.com/contest/2124/problem/A


def solve():
    n = int(input())
    v = list(map(int, input().split()))

    if n == 1:
        print("NO")
        return

    for i in range(n):
        curr_max = v[i]
        for j in range(i + 1, n):
            if v[j] < curr_max:
                print("YES")
                print(2)
                print(curr_max, v[j])
                return
    
    print("NO")


t = int(input())
for _ in range(t):
    solve()


