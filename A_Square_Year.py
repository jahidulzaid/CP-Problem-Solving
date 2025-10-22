# Bismillahir Rahmanir Rahim
# jahidulZaid
# https://codeforces.com/contest/2114/problem/A

def solve_square_years(ls):
    results = []
    for s in ls:
        year = int(s)
        found = False
        for x in range(201):  
            if x * x == year:
                
                a = 0
                b = x
                results.append(f"{a} {b}")
                found = True
                break
        if not found:
            results.append("-1")
    return results


t = int(input())
ls = [input().strip() for _ in range(t)]


for res in solve_square_years(ls):
    print(res)
