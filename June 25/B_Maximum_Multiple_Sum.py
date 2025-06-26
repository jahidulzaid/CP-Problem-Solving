
# jahidulZaid
# https://codeforces.com/contest/1985/problem/B

def max_multiple_sum_x(n):
    max_sum = 0
    best_x = 2
    for x in range(2, n + 1):
        k = n // x
        total = x * k * (k + 1) // 2
        if total > max_sum:
            max_sum = total
            best_x = x
    return best_x


t = int(input())
for _ in range(t):
    n = int(input())
    print(max_multiple_sum_x(n))
