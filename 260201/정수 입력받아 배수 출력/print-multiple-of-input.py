import sys
input = sys.stdin.readline

N = int(input())

for i in range(N, N * 5 + 1, N):
    print(i, end = ' ')