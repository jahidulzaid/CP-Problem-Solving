
# jahidulZaid
# https://codeforces.com/contest/1154/problem/B


def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    unique_a = sorted(set(a))
    k = len(unique_a)
    
    if k == 1:
        print(0)
    elif k == 2:
        diff = unique_a[1] - unique_a[0]
        if diff % 2 == 0:
            print(diff // 2)
        else:
            print(diff)
    elif k == 3:
        if unique_a[1] - unique_a[0] == unique_a[2] - unique_a[1]:
            print(unique_a[1] - unique_a[0])
        else:
            print(-1)
    else:
        print(-1)
solve()
