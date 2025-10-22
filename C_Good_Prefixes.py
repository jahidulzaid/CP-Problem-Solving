
# jahidulzaid
# https://codeforces.com/problemset/problem/1985/C

from collections import Counter
import sys
input = sys.stdin.read

def count_good_prefixes(t, test_cases):
    results = []
    for idx in range(t):
        n = test_cases[idx][0]
        a = test_cases[idx][1]
        total = 0
        count = 0
        freq = Counter()
        for i in range(n):
            total += a[i]
            freq[a[i]] += 1
            if total % 2 == 0:
                target = total // 2
                if freq[target] > 0:
                    count += 1
        results.append(count)
    return results

data = input().split()
index = 0
t = int(data[index])
index += 1
test_cases = []
for _ in range(t):
    n = int(data[index])
    index += 1
    a = list(map(int, data[index:index+n]))
    index += n
    test_cases.append((n, a))

results = count_good_prefixes(t, test_cases)
for res in results:
    print(res)
