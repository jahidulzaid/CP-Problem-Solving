# Bismillahir Rahmanir Rahim
# jahidulZaid
# https://codeforces.com/contest/2123/problem/B



def solveit():

    n, j, k = map(int, input().split())
    v = list(map(int, input().split()))
    
    val = v[j - 1]
    v.sort()
    mx = v[-1]
    
    if k >= 2:
        print("YES")
    elif val == mx:
        print("YES")
    else:
        print("NO")

def main():
    t = int(input()) 
    
    for _ in range(t):
        solveit()

if __name__ == "__main__":
    main()