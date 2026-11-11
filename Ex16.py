# TSP - Minimum Cost and Optimal Route using Branch and Bound
n = int(input("Cities: "))
a = [list(map(int, input().split())) for _ in range(n)]
best = float("inf")
route = []

def search(city, path, cost):
    global best, route
    if cost >= best:
        return
    if len(path) == n:
        if a[city][0] > 0 and cost + a[city][0] < best:
            best = cost + a[city][0]
            route = path + [0]
        return

    for nxt in range(1, n):
        if nxt not in path and a[city][nxt] > 0:
            search(nxt, path + [nxt], cost + a[city][nxt])

search(0, [0], 0)
if route:
    print("Minimum Cost:", best)
    print("Optimal Route:", route)
else:
    print("No possible route")
