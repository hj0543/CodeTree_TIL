n, m = map(int, input().split())

# Please write your code here.

grid = []
for i in range(n):
    grid.append([0] * m)

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

dir_num = [0, 1, 2, 3]
input_dir = 0

r, c = 0, 0

number = 65     # 아스키코드 'A' 65

for i in range(n*m*2):
    grid[r][c] = chr(number)

    cur_dir = input_dir % 4
    nr = r + dr[cur_dir]
    nc = c + dc[cur_dir]

    if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == 0:
        r, c = nr, nc
        number += 1
    else:
        input_dir += 1

for i in range(n):
    print(*grid[i])