import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())

total = a + b + c



print(total, total // 3, total - (total // 3), sep = '\n')