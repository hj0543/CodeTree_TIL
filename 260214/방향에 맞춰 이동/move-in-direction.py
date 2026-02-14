n = int(input())
moves = [tuple(input().split()) for _ in range(n)]
dir = [move[0] for move in moves]           # ['N', 'E', 'S', 'E']
dist = [int(move[1]) for move in moves]     # [3, 2, 1, 2]

# Please write your code here.

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

x, y = 0, 0

for i in range(n):
    for j in range(dist[i]):
        if dir[i] == 'N':
            nx, ny = x + dx[0], y + dy[0]
        elif dir[i] == 'E':
            nx, ny = x + dx[1], y + dy[1]
        elif dir[i] == 'S':
            nx, ny = x + dx[2], y + dy[2]
        else:
            nx, ny = x + dx[3], y + dy[3]
        x, y = nx, ny
print(x, y)           