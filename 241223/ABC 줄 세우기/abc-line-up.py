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
if total == 0:
    print(total)
else: 
    if total %2 != 0:
        print(total-(cnt))
    else:
        print(total-(cnt-1))