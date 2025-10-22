# Bismillahir Rahmanir Rahim
# jahidulZaid
# https://codeforces.com/problemset/problem/2114/C

def max_number_of_arrays(arr):
    last = -2  # last selected element
    count = 0
    for x in arr:
        if x > last + 1:
            count += 1
            last = x
    return count


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    print(max_number_of_arrays(a))

