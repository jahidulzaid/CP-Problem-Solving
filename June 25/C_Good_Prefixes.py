# jahidulzaid
# https://codeforces.com/contest/1985/problem/C


from collections import defaultdict
def gd_prefix(tcases):
    results = []
    for n, arr in tcases:
        prefix_sum = 0
        count = 0
        freq = defaultdict(int)
        for i in range(n):
            prefix_sum += arr[i]
            freq[arr[i]] += 1
            if prefix_sum % 2 == 0:
                target = prefix_sum // 2
                if freq[target] > 0:
                    count += 1
        results.append(count)
    return results

t = int(input())
tcases = []
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    tcases.append((n, arr))


results = gd_prefix(tcases)
for res in results:
    print(res)
