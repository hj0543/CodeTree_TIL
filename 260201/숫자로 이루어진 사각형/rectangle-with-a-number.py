n = int(input())

# Please write your code here.

num = 1

for i in range(n):
    for j in range(n):
        print(num, end=' ')
        num = num % 9 + 1
    print()