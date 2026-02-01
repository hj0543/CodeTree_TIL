import sys
input = sys.stdin.readline

temperature = int(input())

if temperature >= 100:
    print('vapor')
elif temperature < 0:
    print('ice')
else:
    print('water')