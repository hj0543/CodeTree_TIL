a, o, c = input().split()
a = int(a)
c = int(c)

# Please write your code here.
def cal(x, k, y):
    if k == '*':
        return x * y
    elif k == '/':
        return x // y
    elif k == '+':
        return x + y
    elif k == '-':
        return x - y
    else:
        return False

if cal(a, o, c):
    print(f'{a} {o} {c} = {cal(a, o, c)}')
else:
    print(False)