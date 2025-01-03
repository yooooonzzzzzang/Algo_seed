n = int(input())
arr = list(input().split())

# Write your code here!
nums = [0] * 10
k = max(len(str(i)) for i in arr)

for i in range(k):
    pos = i
    for j in range(n):
        # if 문 추가
        
        nums [int(arr[j][i])] = int(arr[j][i])
    arr = []
    for j in range(10):
        # 0 빼고 arr 대입
        if nums[j] != 0:
           arr.append(str(nums[j]))
    nums = [0] * 10 
print(*arr)