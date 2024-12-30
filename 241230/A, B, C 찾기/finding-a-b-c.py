arr = list(map(int,input().split()))

arr.sort()
a = arr[0]
b = arr[1]
abc =arr[-1]
print(a, b,abc-a-b)