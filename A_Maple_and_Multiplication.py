import math

def min_operations(a, b):
    if a == b:
        return 0
    lcm = a * b // math.gcd(a, b)
    return int(lcm != a) + int(lcm != b)

t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    print(min_operations(a, b))
