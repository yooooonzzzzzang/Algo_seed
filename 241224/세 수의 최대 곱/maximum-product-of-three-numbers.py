#  - - + 
# + + + 
# 0 이 있는 경우 
n = int(input())

arr = list(map(int,input().split()))

arr.sort()


if arr[1] < 0 :
    print(max(arr[0] * arr[1] * arr[-1], arr[-1]*arr[-2]*arr[-3]))
else:
    print(arr[-1]*arr[-2]*arr[-3])