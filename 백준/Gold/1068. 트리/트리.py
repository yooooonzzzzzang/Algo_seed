import sys
input = sys.stdin.readline
n = int(input())
tree = list(map(int, input().split()))
delete_n = [int(input())]
# 1. 제거하는거
# 2. 리프노드인지 확인
def dfs(i):
    delete_n.append(i)
    tree[i] = ""
    for idx in range(n):
        if i == tree[idx]:
            dfs(idx)
tree[delete_n[0]] = ""
dfs(delete_n[0])

cnt = 0
for i in range(n):
    if tree[i] == "":
        continue
    if i not in tree:
        cnt+=1
print(cnt)
