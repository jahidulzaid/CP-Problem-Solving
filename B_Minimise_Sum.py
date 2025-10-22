# Bismillahir Rahmanir Rahim
# jahidulZaid
# https://codeforces.com/contest/2124/problem/B

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    best_sum = 0
    current_min = float('inf')
    for val in a:
        current_min = min(current_min, val)
        best_sum += current_min
    
    for j in range(1, n):
        for i in range(j):
            temp_sum = 0
            prefix_min_val = float('inf')
            
            for k in range(j):
                val = a[k]
                if k == i:
                    val += a[j]
                
                prefix_min_val = min(prefix_min_val, val)
                temp_sum += prefix_min_val
            
            best_sum = min(best_sum, temp_sum)

    print(best_sum)