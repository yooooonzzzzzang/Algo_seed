def combinations(arr,start,cnt):
    if len(arr) == cnt:
        print(*arr)
        return
    for i in range(start, n):
        arr.append(nums[i])
        combinations(arr, i+1, cnt)
        arr.pop()
n,m = map(int,input().split())

nums = [i for i in range(1, n+1)]

combinations([],0,m)