t = int(input())
for _ in range(t):
    n, m, l, r = map(int, input().split())
    diff = n - m
    l_prime = l + diff
    r_prime = r - diff
    print(l_prime, r_prime)
