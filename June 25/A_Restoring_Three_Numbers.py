
# jahidulZaid
# https://codeforces.com/contest/1352/problem/B


p,q,r,s = map(int, input().split())

list = []

list.append(p)
list.append(q)
list.append(r)
list.append(s)
x = list
x.sort()

sum_abc = x[3]
a = sum_abc - x[2]
b = sum_abc - x[1]
c = sum_abc - x[0]

print(a, b, c)



    



