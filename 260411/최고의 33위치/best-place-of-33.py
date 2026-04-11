n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

def search_grid(r, c):
    coins = 0
    for i in range(3):
        coins += sum(grid[r+i][c:c+3])
    return coins

max_coins = 0
for r in range(n-2):
    for c in range(n-2):
        max_coins = max(max_coins, search_grid(r, c))

print(max_coins)
