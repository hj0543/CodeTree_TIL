import sys
input = sys.stdin.readline

word = input().rstrip()

result = []

for i in range(8):
    result.append(word)

print(''.join(result))
