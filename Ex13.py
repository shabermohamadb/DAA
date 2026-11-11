# Warshall's Algorithm using Adjacency Matrix
n = int(input("Vertices: "))
a = [list(map(int, input().split())) for _ in range(n)]

for k in range(n):
    for i in range(n):
        for j in range(n):
            if a[i][k] and a[k][j]:
                a[i][j] = 1

print("Transitive Closure:")
for row in a:
    print(*row)
