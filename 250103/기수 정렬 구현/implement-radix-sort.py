n = int(input())
arr = list(input().split())

# Write your code here!
k = max(len(str(i)) for i in arr)

for i in range(k):
      # 0~9 버킷을 만듦
    buckets = [[] for _ in range(10)]
    for num in arr:
        if len(num) <= i:
            digit = 0
        else:
            digit = int(num[-(i+1)])
        buckets[digit].append(num)
    arr = []
    for numbers in buckets:
        for number in numbers:
            arr.append(number)
print(*arr)