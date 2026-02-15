n = int(input())
grid = [[0] * n for _ in range(n)]

# Please write your code here.
center_n = (n // 2)

dr = [0, -1, 0, 1]
dc = [1, 0, -1, 0]

cur_dir = 0   # 현재 방향
dist = 1      # 이동해야 할 거리 (1, 1, 2, 2, 3, 3...)
cnt = 0       # 현재 방향으로 이동한 횟수 카운트
turn_cnt = 0  # 방향 전환 횟수 (2번 바꿀 때마다 dist 증가)
r, c = center_n, center_n


number = 1
grid[r][c] = number # 시작점 1 찍기

while number < n * n:

    nr = r + dr[cur_dir]
    nc = c + dc[cur_dir]
    
    if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0:
        grid[nr][nc] = number + 1
        r, c = nr, nc
        number += 1
        cnt += 1

    # 방향 전환 규칙
    if cnt == dist:
        cur_dir = (cur_dir + 1) % 4 # 방향 전환
        cnt = 0                     # 이동 횟수 초기화
        turn_cnt += 1               # 방향 전환 횟수 증가
        
        # 두 번 방향을 바꿨다면, 이동 거리(dist) 1 증가
        if turn_cnt % 2 == 0:
            dist += 1














for i in range(n):
    print(*grid[i])

