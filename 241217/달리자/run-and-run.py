n =int(input())
arr1 = list(map(int,input().split()))
arr2 = list(map(int,input().split()))
cnt =0
for i in range(n):
    if arr1[i] > arr2[i]:
        tmp = arr1[i] - arr2[i]
        arr1[i] -= tmp
        arr1[i+1] += tmp
        cnt += tmp

print(cnt)