h, w = map(int, input().split())
arr =list(map(int, input().split()))
area = sum(arr)
square_area = h* w
prefix = [0] * (w+3)
max_w = arr.index(max(arr))
for i in range(max_w):
    prefix[i+1] = max(prefix[i], arr[i])
for i in range(w-1, max_w-1, -1):
    prefix[i+1] = max(prefix[i+2], arr[i])
platten = sum(prefix)
print(square_area - area - (square_area - platten))