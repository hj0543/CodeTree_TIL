n, m = map(int, input().split())

# Please write your code here.

grid = []
for i in range(n):
    grid.append([0] * m)

dr = [1, 0, -1, 0]
dc = [0, 1, 0 ,-1]

dir_num = [0, 1, 2, 3]
input_dir = 0

r, c = 0, 0

number = 1
for i in range(n*m*2):          # 여유롭게 2배만큼
    grid[r][c] = number         # 현재 위치에 숫자 기록
    if grid[r][c] == n * m:     # 숫자 다 채웠으면 종료
        break
    cur_dir = input_dir % 4     # 현재 방향 설정
    nr = r + dr[cur_dir]        # 델타탐색 수식
    nc = c + dc[cur_dir]

    if 0 <= nr < n and 0 <= nc < m:    # 이동하고자 하는 곳이 범위 안이라면
        if grid[nr][nc] == 0:          # 이동하고자 하는 곳의 값이 0이라면
            r, c = nr, nc              # 이동
            number += 1                # 기록할 숫자 +1
        else:
            input_dir += 1             # 아니면 방향 돌리기
    else:
        input_dir += 1

for i in range(n):
    print(*grid[i])







