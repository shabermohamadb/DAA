# Topological Sort - Decrease and Conquer (Kahn's Algorithm)
n = int(input("Vertices: "))
a = [list(map(int, input().split())) for _ in range(n)]

indegree = [sum(a[i][j] for i in range(n)) for j in range(n)]
order = []

for _ in range(n):
    for i in range(n):
        if indegree[i] == 0:
            order.append(i)
            indegree[i] = -1
            for j in range(n):
                if a[i][j]:
                    indegree[j] -= 1
            break

if len(order) == n:
    print("Topological Order:", order)
else:
    print("Graph contains a cycle")
