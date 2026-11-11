# Topological Sort using Depth First Search
n = int(input("Vertices: "))
a = [list(map(int, input().split())) for _ in range(n)]
visited = [0] * n
order = []

def dfs(v):
    visited[v] = 1
    for i in range(n):
        if a[v][i] and not visited[i]:
            dfs(i)
    order.append(v)

for i in range(n):
    if not visited[i]:
        dfs(i)

print("Topological Order:", order[::-1])
