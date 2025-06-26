
# jahidulZaid
# https://codeforces.com/contest/2112/problem/D

def dfs(node, parent, color, graph, result):
    for child in graph[node]:
        if child != parent:
            if color % 2 == 1:
                result.append((node, child))
            else:
                result.append((child, node))
            dfs(child, node, 1 - color, graph, result)

def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        graph = [[] for _ in range(n + 1)]
        result = []

        for _ in range(n - 1):
            x, y = map(int, input().split())
            graph[x].append(y)
            graph[y].append(x)

        if n == 2:
            print("NO")
            continue

        root = -1
        for i in range(1, n + 1):
            if len(graph[i]) == 2:
                root = i
                break

        if root == -1:
            print("NO")
            continue

        u, v = graph[root][0], graph[root][1]
        result.append((root, u))
        result.append((v, root))

        dfs(u, root, 0, graph, result)
        dfs(v, root, 1, graph, result)

        print("YES")
        for x, y in result:
            print(x, y)

solve()
