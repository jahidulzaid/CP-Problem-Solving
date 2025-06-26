# jahidulZaid
# https://codeforces.com/contest/2120/problem/A

def solve():
    l1, b1, l2, b2, l3, b3 = map(int, input().split())

    def can_fill(target_L, target_B, r2_l, r2_b, r3_l, r3_b):
        if (r2_l + r3_l == target_L and r2_b == target_B and r3_b == target_B):
            return True
        if (r2_l == target_L and r3_l == target_L and r2_b + r3_b == target_B):
            return True
        return False

    res = False

    S1 = l1
    if S1 > b1:
        if can_fill(S1, S1 - b1, l2, b2, l3, b3):
            res = True

    if not res:
        S2 = b1
        if S2 > l1:
            if can_fill(S2 - l1, S2, l2, b2, l3, b3):
                res = True
    
    if res:
        print("YES")
    else:
        print("NO")

t = int(input())
for _ in range(t):
    solve()