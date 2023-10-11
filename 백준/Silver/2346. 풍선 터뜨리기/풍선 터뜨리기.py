'''
5
3 2 1 -3 -1
'''
# 원형리스트 == deque
from collections import deque

n = int(input())
q = deque(enumerate(map(int, input().split())))
ans = []

while q:
    # 왼쪽으로 한칸 움직임
    idx, paper = q.popleft()
    ans.append(idx + 1)
    # 양수 -> 왼쪽으로 움직여야함 -> Rotate 음수
    if paper > 0:
        q.rotate(-(paper -1))
    # 음수 -> 오른쪽으로 움직여야함 -> rotate 양수
    elif paper < 0:
        q.rotate(-paper)
print(*ans)

