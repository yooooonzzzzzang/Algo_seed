def solution(arr , cnt):
    if len(arr) == cnt:
        print(*arr)
        return
    for i in range(n):
        arr.append(nums[i])
        solution(arr, cnt)
        arr.pop()



n, m = map(int, input().split())
nums = [i for i in range(1, n+1)]
solution([], m)