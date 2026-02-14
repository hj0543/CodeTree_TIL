a, b = map(int, input().split())

# Please write your code here.
def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return True
    else:
        return False

total = 0
for i in range(a, b + 1):
    if not is_prime(i):
        total += i

print(total)




