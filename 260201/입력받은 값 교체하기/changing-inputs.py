import sys
input = sys.stdin.readline

a , b = map(int, input().split())

c = b
b = a
a = c

print(a, b, sep = ' ')