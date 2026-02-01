import sys
input = sys.stdin.readline

A, N = map(int, input().split())

for i in range(N):
    print(A + (N * (i + 1)))