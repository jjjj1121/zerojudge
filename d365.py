from collections import defaultdict
def dfs(m, i, j, v, l):
    if i < 0 or i >= len(m) or j < 0 or j >= len(m[0]):
        return
    if (i, j) in v:
        return
    if m[i][j] != l:
        return
    v.add((i, j))
    dfs(m, i-1, j, v, l)
    dfs(m, i+1, j, v, l)
    dfs(m, i, j-1, v, l)
    dfs(m, i, j+1, v, l)
def count_ls(m):
    count_dict = defaultdict(int)
    v = set()
    for i in range(len(m)):
        for j in range(len(m[0])):
            l = m[i][j]
            if (i, j) not in v:
                dfs(m, i, j, v, l)
                count_dict[l] += 1
    return count_dict
N = int(input())
for k in range(1, N+1):
    H, W = map(int, input().split())
    m = []
    for _ in range(H):
        row = input().strip()
        m.append(list(row))
    count_dict = count_ls(m)
    print(f"World #{k}")
    for l, count in sorted(count_dict.items(), key=lambda x: (-x[1], x[0])):
        print(f"{l}: {count}"))):        print(f"{l}: {count}")