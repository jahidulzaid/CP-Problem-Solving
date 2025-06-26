
# jahidulZaid
# https://codeforces.com/problemset/problem/1352/A

def solve():
    n = int(input())
    
    round_numbers = []
    power_of_10 = 1
    
    while n > 0:
        digit = n % 10
        if digit != 0:
            round_numbers.append(digit * power_of_10)
        n //= 10
        power_of_10 *= 10
        
    print(len(round_numbers))
    print(*round_numbers)

t = int(input())
for _ in range(t):
    solve()
    