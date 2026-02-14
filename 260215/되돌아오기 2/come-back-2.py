commands = list(map(str, input().rstrip()))

# Please write your code here.

dir_num = [0, 1, 2, 3]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

input_dir = 0
x, y = 0, 0

sec = 0
for i in range(len(commands)):
    cur_dir = (input_dir + 4) % 4   # 꼭 for 반복문 안으로 집어넣기!!
    nx = x + dx[cur_dir]
    ny = y + dy[cur_dir]
    if commands[i] == 'R':
        input_dir += 1
        sec += 1
    elif commands[i] == 'L':
        input_dir -= 1
        sec += 1
    else:
        x, y = nx, ny
        sec += 1
        if x == 0 and y == 0:
            print(sec)
            exit()

else:
    print(-1)