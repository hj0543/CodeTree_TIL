K, N = map(int, input().split())

# Please write your code here.
path = []
def get_numbers():
    if len(path) == N:
        print(*path)
        return
    
    for i in range(1, K + 1):
        path.append(i)
        get_numbers()
        path.pop()

get_numbers()