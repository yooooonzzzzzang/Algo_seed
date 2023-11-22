import sys

input = sys.stdin.readline
n = int(input())
buildings = []
ans = 0

for _ in range(n):
    buildings.append(int(input()))
# 볼 친구들을 stack 에 넣는다
stack = []

for b in buildings:
    while stack and stack[-1] <= b:
        stack.pop()
    stack.append(b)
    ans += len(stack) - 1

print(ans)