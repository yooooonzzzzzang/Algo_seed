n = int(input())
arr = []
for _ in range(n):
    a, b = map(int, input().split())
    arr.append([a,b])
arr.sort(key=lambda x:x[1])
if n == 1:
    print(1)
else:
    cnt = 1
    first = arr[0][1]
    for i in range(1,n):
        if first < arr[i][0] :
            cnt += 1
            first = arr[i][1]
    print(cnt)
# Please write your code here.
