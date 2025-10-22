t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(reverse=True)

    k = min(n, m)
    answer = 0
    for i in range(k):
        answer += a[i] * (m - i)
    print(answer)
