'''
5
1 2
2 3
3 4
4 5
4
1 1
1 2
2 1
2 2
'''

import sys

input = sys.stdin.readline
n = int(input())
tree = [[] for _ in range(n+1)]
for _ in range(n-1):
    v1, v2 = map(int,input().split())
    tree[v1].append(v2)
    tree[v2].append(v1)
for _ in range(int(input())):
    t, k = map(int, input().split())
    if t == 1:
        if len(tree[k]) >= 2:
            print("yes")
        else:
            print("no")
    else: # 사이클이 존재하지 않고 모든 정점이 연결되어 있으므로 간선 제거시 무조건 나눠진다.
        print("yes")
