def queen(state, row):
    if row == 8: 
        global ans
        ans = max(ans, sum([matrix[state[i]][i] for i in range(8)]))
        return

    for col in range(8):
        if col in state or any(abs(state[i]-col)==abs(i-row) for i in range(row)):
            continue
        queen(state + [col], row+1)

for i in range(int(input())):
    matrix = [list(map(int, input().split())) for _ in range(8)]
    ans = 0
    queen([], 0)
    print(f'{ans: <5}')