
# jahidulZaid
# https://codeforces.com/contest/2112/problem/D


def solve():

  a, b = input().split()
  
 
  new_a = b[0] + a[1:]
  new_b = a[0] + b[1:]
  
  print(new_a, new_b)



t = int(input())
for _ in range(t):
    solve()
