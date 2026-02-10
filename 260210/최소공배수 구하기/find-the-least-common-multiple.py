n, m = map(int, input().split())

# Please write your code here.

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return abs(a * b) // gcd(a, b)


print(lcm(n, m))