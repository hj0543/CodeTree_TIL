n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

total = 0
for i in range(n):
    for j in range(n):
        add = 0
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < n and 0 <= nj < n:
                if grid[ni][nj] == 1:
                    add += 1
        if add >= 3:
            total += 1

print(total)









