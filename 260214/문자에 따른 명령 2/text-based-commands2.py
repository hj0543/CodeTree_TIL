cmd = list(map(str, input().rstrip()))

# Please write your code here.
def dirs(s, dir_num):
    if s == 'L':
            dir_num = (dir_num + 3) % 4
    elif s == 'R':
        dir_num = (dir_num + 1) % 4
    return dir_num

dir_num = 0 # 4로 하면 런타임에러남

# D =북  동  남  서
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

x, y = 0, 0

for i in range(len(cmd)):
    if cmd[i] == 'F':
        x += dx[dir_num]
        y += dy[dir_num]
    else:
        dir_num = dirs(cmd[i], dir_num)

print(x, y)



