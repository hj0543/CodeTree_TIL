n = int(input())

# Please write your code here.
def num_sum(n):
    total = 0
    for i in str(n):
        total += int(i)
    return total

def magic_number(n):
    if n % 2 == 0 and num_sum(n) % 5 == 0:
        return 'Yes'
    else:
        return 'No'

print(magic_number(n))