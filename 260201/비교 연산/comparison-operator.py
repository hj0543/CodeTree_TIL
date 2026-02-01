import sys
input = sys.stdin.readline

A, B = map(int, input().split())

cond = [A >= B, A > B, B >= A, B > A, A == B, A != B]


for i in range(6):
    if cond[i]:
        print(1)
    else:
        print(0)