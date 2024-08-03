def bfs():
    q = [S]
    visited[S[0]][S[1]][S[2]] = 1
    while q:
        x, y, z, t = q.pop(0)
        if x == E[0] and y == E[1] and z == E[2]:
            return t
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if nx >= 0 and nx < L and ny >= 0 and ny < R and nz >= 0 and nz < C and a[nx][ny][nz] != '#' and visited[nx][ny][nz] == 0:
                q.append((nx, ny, nz, t+1))
                visited[nx][ny][nz] = 1
    return -1

a = [[[None for _ in range(31)] for _ in range(31)] for _ in range(31)]
visited = [[[0 for _ in range(31)] for _ in range(31)] for _ in range(31)]
dx = [0, 0, 0, 0, 1, -1]
dy = [0, 0, 1, -1, 0, 0]
dz = [1, -1, 0, 0, 0, 0]
 
while True:
    L, R, C = map(int, input().split())
    if L == 0 and R == 0 and C == 0:
        break
 
    for i in range(L):
        for j in range(R):
            a[i][j] = list(input())
            for k in range(C):
                visited[i][j][k] = 0
                if a[i][j][k] == 'S':
                    S = (i, j, k, 0)
                if a[i][j][k] == 'E':
                    E = (i, j, k)
        _ = input() #在一層描述完後有一列空白區隔
 
    Time = bfs()
    if Time != -1:
        print(f"Escaped in {Time} minute(s).")
    else:
        print("Trapped!")