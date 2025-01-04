n = int(input())
arr = list(map(int, input().split()))




def merge(s,mid,e):
    i = s
    j = mid + 1

    k = s
    while i<=mid and j<=e:
        if arr[i] <= arr[j]:
            sorted_arr[k] = arr[i]
            k+=1
            i+=1
        else:
            sorted_arr[k] = arr[j]
            k+=1
            j+=1
    
    while i<=mid:
        sorted_arr[k] = arr[i]
        k+=1
        i+=1
    
    while j<=e:
        sorted_arr[k] = arr[j]
        k+=1
        j+=1
    for k in range(s,e+1):
        arr[k] = sorted_arr[k]

    return arr
def merge_sort(s,e):
    if s < e:
        mid = (s + e) // 2
        merge_sort(s, mid)
        merge_sort(mid+1, e)
        merge(s,mid,e)
sorted_arr = [0] * n

merge_sort(0,n-1)
print(*arr)
