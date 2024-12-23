ans = -1
n = int(input())
arr= list(map(int, input().split()))

sortedArr = sorted(arr)
setArr = set(sortedArr)
if len(setArr) >=2:
    target = tuple(setArr)[1]
    if arr.count(target) >= 2:
        print(-1)
    else:
        print(arr.index(target) +1)
else:
    print(-1)