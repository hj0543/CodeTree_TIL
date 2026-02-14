y = int(input())

# Please write your code here.
def leap_year(n):
    if n % 4 != 0:
        return 'false'
    if n % 100 == 0:
        if n % 400 != 0:
            return 'false'
        else:
            return 'true'
    return 'true'

print(leap_year(y))
