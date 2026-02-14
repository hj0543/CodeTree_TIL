n, m = map(int, input().split())
arr = [[0] * m for _ in range(n)]

# Please write your code here.

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

dir_num = 0


x, y = 0, 0
num = 1

for i in range(1, n * m * 2):
    cur_dir = dir_num % 4   # 반복문 안으로 집어넣어야 함!!
    nx = x + dx[cur_dir]
    ny = y + dy[cur_dir]
    arr[y][x] = num
    if 0 <= nx < m and 0 <= ny < n and arr[ny][nx] == 0:
        x, y = nx, ny
        num += 1
    else:
        dir_num += 1

for i in range(n):
    print(*arr[i])













