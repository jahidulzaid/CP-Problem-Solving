# Bismillahir Rahmanir Rahim
# Jahidul Islam, Green University Of Bangladesh
# @JahidulZaid

# p = lambda: list(map(float, input().split()))
p = lambda: list(map(int, input().split()))

n, t = p()
l = p()
i = j = s = max_books = 0
for j in range(n):
    s += l[j]
    while s > t:
        s -= l[i]
        i += 1
    max_books = max(max_books, j - i + 1)
print(max_books)
