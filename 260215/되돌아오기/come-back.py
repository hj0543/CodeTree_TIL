N = int(input())
moves = [tuple(input().split()) for _ in range(N)]
dir = [move[0] for move in moves]
dist = [int(move[1]) for move in moves]

# Please write your code here.

dir_dict = {
    'N' : 0,
    'E' : 1,
    'S' : 2,
    'W' : 3
}

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

x, y = 0, 0

cur_pos = []
cnt = 0

for i in range(N):
    for j in range(dist[i]):
        nx = x + dx[dir_dict[dir[i]]]
        ny = y + dy[dir_dict[dir[i]]]
        x, y = nx, ny
        cnt += 1
        if x == 0 and y == 0:
            print(cnt)
            exit()
else:
    print(-1)











