'''
6 7
1
5
3
3
5
1
'''
import sys
input = sys.stdin.readline
n, h = map(int, input().split())
arr = [0] * h

prefix = [0] * (h+1)
for i in range(n):
    # 짝수면 왼쪽부터
    k = int(input())
    if i % 2 == 0:
        arr[0] += 1
        arr[k] -= 1
    if i % 2 == 1:
        arr[h-k] += 1

for i in range(h):
    prefix[i+1] = (prefix[i]+arr[i])
prefix= prefix[1:]
print(min(prefix), prefix.count(min(prefix)))

