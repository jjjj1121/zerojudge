def dfs(node, color, graph, colors):
    colors[node] = color
    for neighbor in graph[node]:
        if colors[neighbor] == color:
            return False
        if colors[neighbor] == 0 and not dfs(neighbor, -color, graph, colors):
            return False
    return True

while True:
    n = int(input())
    if n == 0:
        break
    m = int(input())
    graph = {i: [] for i in range(n)}
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    colors = [0] * n
    if dfs(0, 1, graph, colors):
        print("BICOLORABLE.")
    else:
        print("NOT BICOLORABLE.")