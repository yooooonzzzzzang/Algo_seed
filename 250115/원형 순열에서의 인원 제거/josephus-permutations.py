from collections import deque
n, k = map(int, input().split())
dq = deque()
for i in range(1,n+1):
    dq.append(i)
while dq :
    for i in range(k-1):
        dq.append(dq.popleft())
    print(dq.popleft(), end=" ")
# Write your code here!
