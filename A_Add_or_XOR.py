# Bismillahir Rahmanir Rahim
# Jahidul Islam, Green University Of Bangladesh
# @JahidulZaid

def min_cost_to_make_equal(t, test_cases):
    res = []
    for a, b, x, y in test_cases:
        if a == b:
            res.append(0)
            continue
        ans = float('inf')
        if a <= b:
            ans = min(ans, (b - a) * x)
        new_a = a ^ 1
        if new_a <= b:
            ans = min(ans, y + (b - new_a) * x)
        new_a = (a + 1) ^ 1
        if new_a <= b:
            ans = min(ans, x + y + (b - new_a) * x)
        new_a = (a ^ 1) ^ 1
        if new_a <= b:
            ans = min(ans, 2 * y + (b - new_a) * x)
        if ans == float('inf'):
            res.append(-1)
        else:
            res.append(ans)
    return res

t = 7
test_cases = [
    (1, 4, 1, 2),
    (1, 5, 2, 1),
    (3, 2, 2, 1),
    (1, 3, 2, 1),
    (2, 1, 1, 2),
    (3, 1, 1, 2),
    (1, 100, 10000000, 10000000)
]

output = min_cost_to_make_equal(t, test_cases)
for val in output:
    print(val)
