n, t = map(int, input().split()) # 4 4
r, c, d = input().split() # 1 2 L
r, c = int(r), int(c)

# Please write your code here.

directions = {
    'R' : 0,
    'D' : 1,
    'U' : 2,
    'L' : 3
}

dr = [0, 1, -1, 0]
dc = [1, 0, 0, -1]
cur_dirs = directions[d]

for i in range(t):
    nr, nc = r + dr[cur_dirs], c + dc[cur_dirs]
    if 1 <= nr <= n and 1 <= nc <= n:
        r, c = nr, nc
    else:
        cur_dirs = 3 - cur_dirs
 
print(r, c)










