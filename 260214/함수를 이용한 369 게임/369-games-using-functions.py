a, b = map(int, input().split())

# Please write your code here.
def function1(n):
    if ('3' in str(n)) or ('6' in str(n)) or ('9' in str(n)):
        return True
    elif n % 3 == 0:
        return True

total = 0
for i in range(a, b+1):
    if function1(i):
        total += 1    
    
print(total)


