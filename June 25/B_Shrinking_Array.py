# jahidulzaid
# https://codeforces.com/contest/2112/problem/B

def solve():
    n = int(input())
    a = list(map(int, input().split()))


    for i in range(n -1):
        if abs(a[i] - a[i+1]) <= 1:
            print(0)
            return
    
    #by 1 op
    if n ==2:
        print(-1)
        return
    
    for k in range(n -1):
        L = min(a[k], a[k+1])
        R = max(a[k], a[k+1])

        if k>0:
            if max(L, a[k-1] -1) <= min(R, a[k-1] +1):
                print(1)
                return
        if k+2 < n:
            if max(L, a[k+2] -1) <= min(R, a[k+2]+1):
                print(1)
                return
    print(-1) # !1


t = int(input())
for _ in range(t):
    solve()
