n = int(input())
arr = list(map(int,input().split()))

for i in range(1,n):
    # 지금까지 합한게 더 큰지, 현재가 더 큰지 max 만 기록
    arr[i] = max(arr[i], arr[i-1]+arr[i])
print(max(arr))