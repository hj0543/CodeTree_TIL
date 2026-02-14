n, m = map(int, input().split())
points = [list(map(int, input().split())) for _ in range(m)]
# [(1, 2), (2, 1), (2, 3), (2, 2), (3, 3), (4, 2), (3, 2), (4, 3)]

# Please write your code here.

grid = []
for i in range(n+1):
    grid.append([0] * (n + 1))

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

result = [0] * m


for k in range(m):
    grid[points[k][0]][points[k][1]] = 1
    cnt = 0

    for l in range(4):
        ni = points[k][0] + di[l]
        nj = points[k][1] + dj[l]
        
        if 1 <= ni <= n and 1 <= nj <= n:
            if grid[ni][nj] == 1:
                cnt += 1
    if cnt == 3:
        result[k] = 1

for i in range(m):
    print(result[i])










