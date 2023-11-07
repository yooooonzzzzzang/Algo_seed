'''
7
1 6
6 3
3 5
4 1
2 4
4 7
'''
# 루트 1
import sys
sys.setrecursionlimit(100000000)
n = int(input())
graph = [[] for _ in range(n+1)]
graph2 = [[] for _ in range(n+1)]
for _ in range(n-1):
    n1, n2 = map(int, input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)

def resort(node):
    for nxt in graph[node]:
        graph[nxt].remove(node)
        resort(nxt)
resort(1)
for i in range( n+1):
    for chs in graph[i]:
        graph2[chs].append(i)
for i in range(2, n+1):
    for chs in graph2[i]:
        print(chs)