n = int(input())
arr1 = sorted(list(map(int, input().split())))
m = int(input())
arr2 = list(map(int, input().split()))
# python in O(n) / binary search O(logN)
for i in range(m):
    s =0
    e = n-1
    flag = False
    while s <= e:
        mid = (s+e)//2
        if arr2[i] == arr1[mid]:
            flag = True
            break
        elif arr1[mid] > arr2[i] :
            e = mid-1
        else:
            s = mid+1
    if flag:
        print(1, end=" ")
    else:
        print(0, end=" ")

