# Bismillahir Rahmanir Rahim
# Jahidul Islam, Green University Of Bangladesh
# @JahidulZaid

from collections import deque

def gold(n, m):
    if m>n:
        return 0
    if m==n:
        return 1
    
    visited = set()
    q = deque()
    q.append(m)
    visited.add(m)
    while q:
        curr = q.popleft()
        if curr == n:
            return 1
        x1 = 3*curr
        if x1<=n and x1 not in visited:
            visited.add(x1)
            q.append(x1)

        if curr%2 == 0:
            a = curr//2
            if a >= 1:
                x2 = curr +a
                if x2 <= n and x2 not in visited:
                    visited.add(x2)
                    q.append(x2)
    return 0

        

t = int(input())
for _ in range(t):
    n,m = map(int, input().split())
    if gold(n,m):
        print("YES")
    else:
        print("NO")

    