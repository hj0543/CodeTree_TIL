a, b, c = map(int, input().split())
arr = [a, b, c]
# Please write your code here.

def my_min(arr):
    min_v = arr[0]
    for i in range(1, len(arr)):
        if arr[i] < min_v:
            min_v = arr[i]
    return min_v

print(my_min(arr))