import sys
input = sys.stdin.readline

A, B = map(float, input().split())

print(int(A + B), (A + B) / 2, sep = ' ')