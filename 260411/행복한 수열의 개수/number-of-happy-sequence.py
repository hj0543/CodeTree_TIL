n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

happy_seq_counts = 0

for r in range(n):
    temp_row = []
    found = False
    for c in range(n):
        if len(temp_row) >= m:
            happy_seq_counts += 1
            found = True
            break
        if temp_row:
            if temp_row[-1] == grid[r][c]:
                temp_row.append(grid[r][c])
            else:
                temp_row.clear()
                temp_row.append(grid[r][c])
        else:
            temp_row.append(grid[r][c])
    if not found:    
        if len(temp_row) == m:
            happy_seq_counts += 1
    temp_row.clear()

for c in range(n):
    temp_col = []
    found = False
    for r in range(n):
        if len(temp_col) >= m:
            happy_seq_counts += 1
            found = True
            break
        if temp_col:
            if temp_col[-1] == grid[r][c]:
                temp_col.append(grid[r][c])
            else:
                temp_col.clear()
                temp_col.append(grid[r][c])
        else:
            temp_col.append(grid[r][c])
    if not found:
        if len(temp_col) == m:
            happy_seq_counts += 1
    temp_col.clear()

print(happy_seq_counts)