a,b = map(int,input().split())
c,d = map(int,input().split())
arr = [0] * 101

for i in range(a,b):
    arr[i] = 1
for j in range(c,d):
    arr[j] = 1
print(sum(arr))