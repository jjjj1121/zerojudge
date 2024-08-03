def bfs():
    while q:
        x, y, t = q.pop(0)
        for i in range(num):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and nx < N and ny >= 0 and ny < M and a[nx][ny] ==1 and visited[nx][ny] == 0:
                q.append((nx, ny, t+1))
                visited[nx][ny] = 1
                ans[nx][ny] = t+1;

a = [[None for _ in range(200)] for _ in range(200)] 
visited = [[0 for _ in range(200)] for _ in range(200)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
casenumber = 1;
while True:
    ans = [[0 for _ in range(200)] for _ in range(200)] 
    q = []
    try:
        S = int(input())
        if S==1: 
            num = 4
        elif S == 2:
            num = 3
        N, M = map(int, input().split())
        for i in range(N):
            a[i] = list(map(int,input().split()))
            for j in range(M):
                visited[i][j] = 0
        for i in range(M):
            if a[0][i] ==1:
                nextnode = (0,i,1)
                ans[0][i] = 1;
                q = [nextnode]
                visited[nextnode[0]][nextnode[1]] = 1
                bfs()
        print("Case {}:".format(casenumber))
        casenumber +=1
        for i in range(N):
            for j in range(M):
                if j == M-1:
                    print(ans[i][j],end ="\n")
                else:
                    print(ans[i][j],end =" ")
    except:
        break;