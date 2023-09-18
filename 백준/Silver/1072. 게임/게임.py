'''
10 8

'''
import math

x, y = map(int, input().split())


win_rate = (y * 100) // x
start, end = 1, 1000000000

if win_rate >= 99:
    print(-1)
    exit(0)
answer = 0
while start <= end:
    mid = (start + end) // 2
    if int((y + mid) * 100 / (x + mid)) > win_rate:
        answer = mid
        end =  mid-1
    else:
        start = mid + 1

print(answer)
