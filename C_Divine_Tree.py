import sys
import math

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    min_sum = n
    max_sum = n * (n + 1) // 2

    if m < min_sum or m > max_sum:
        print(-1)
        continue

    parent = [0] * (n + 1)
    parent[1] = 0
    diff = m - min_sum

    for i in range(2, n + 1):
        best = 1
        for j in range(1, int(math.sqrt(i)) + 1):
            if i % j == 0:
                for div in [j, i // j]:
                    inc = div - 1
                    if diff >= inc:
                        if best < div:
                            best = div
        parent[i] = best
        diff -= (best - 1)

    print(1)
    for i in range(2, n + 1):
        print(parent[i], i)
