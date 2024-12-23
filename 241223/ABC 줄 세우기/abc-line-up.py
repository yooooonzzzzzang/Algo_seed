n = int(input())
cnt = 0
total = 0

arr = list(input().split())
for i in range(n):
    tmp = (abs(ord(arr[i]) - (65+i )))
    if tmp != 0:
        total += tmp
        cnt += 1
# print(total)
# print(cnt)
print(total-(cnt-1))