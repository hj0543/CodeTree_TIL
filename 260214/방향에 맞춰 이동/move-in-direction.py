n = int(input())
moves = [tuple(input().split()) for _ in range(n)]
dir = [move[0] for move in moves]           # ['N', 'E', 'S', 'E']
dist = [int(move[1]) for move in moves]     # [3, 2, 1, 2]

# Please write your code here.


pos = [0, 0]
for i in range(n):
    for j in range(dist[i]):
        if dir[i] == 'N':
            pos[1] += 1
        elif dir[i] == 'E':
            pos[0] += 1
        elif dir[i] == 'S':
            pos[1] -= 1
        else:
            pos[0] -= 1 

print(*pos)           