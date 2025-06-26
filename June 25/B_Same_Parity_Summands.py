
# jahidulZaid
# https://codeforces.com/contest/1352/problem/B

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())

    #odd
    if n>= k and n%2 ==  k%2:
        print("YES")
        res = [1]*(k-1)
        res.append(n-(k-1))
        print(*res)
    #even
    elif n >= 2*k and n%2 == 0:
        print("YES")
        res = [2]*(k-1)
        res.append(n-2 *(k-1))
        print(*res)
    else:
        print("NO")