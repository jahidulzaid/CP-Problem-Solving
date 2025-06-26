
# jahidulZaid
# https://codeforces.com/contest/1352/problem/B

def solve():
    n, k = map(int, input().split())
    l = 1
    h = 2*10**9

    ans = -1

    while l <= h:
        m = (l + h) // 2

        countNonDiv = m -(m//n)

        if countNonDiv >= k:
            ans = m
            h = m -1
        else:
            l = m +1
    print(ans)




t = int(input())
for _ in range(t):
    solve()
#     n, k = map(int, input().split())
    
#     #not divisible list gen
#     notDivisibleNums = []
#     for num in range(1, k+1):
#         if num % n != 0:
#             notDivisibleNums.append(num)

# print(notDivisibleNums[k])



    
