N, T = map(int, input().split())
commands = input()
board = [list(map(int, input().split())) for _ in range(N)]

# Please write your code here.

start_N = N // 2


dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

dir_num = [0, 1, 2, 3]
input_dir = dir_num[0]


r, c = [start_N, start_N]
path = [board[r][c]]


for cmd in commands:
    cur_dir = (input_dir + 4) % 4
    nr = r + dr[cur_dir]
    nc = c + dc[cur_dir]
    if cmd == 'R':
        input_dir += 1
    
    elif cmd == 'L':
        input_dir -= 1

    else:
        if 0 <= nr < N and 0 <= nc < N:
            r, c = nr, nc
            path.append(board[r][c])

print(sum(path))






