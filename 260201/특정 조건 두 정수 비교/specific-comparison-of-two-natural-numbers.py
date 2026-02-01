import sys
input = sys.stdin.readline

A, B = map(int, input().split())

if A < B:
    result1 = 1
else:
    result1 = 0

if A == B:
    result2 = 1
else:
    result2 = 0

print(result1, result2, sep = ' ')