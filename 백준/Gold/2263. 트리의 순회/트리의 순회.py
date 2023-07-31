'''
3
1 2 3
1 3 2
'''
import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
def preorder(in_start, in_end, post_start, post_end):
    # 종료 조건
    if (in_start > in_end) or (post_start > post_end):
        return
    # 후위 순회의 끝이 루트
    parent = postorder[post_end]
    print(parent, end =" ")

    # 중위순회의 l root r
    left = position[parent] - in_start
    right = in_end - position[parent]
    # 왼, 오
    preorder(in_start, in_start+left-1, post_start, post_start+left-1)
    preorder(in_end-right+1, in_end, post_end-right, post_end-1)
n = int(input())
inorder = list(map(int,input().split()))
postorder = list(map(int,input().split()))
position = [0] * (n+1)
for i in range(n):
    position[inorder[i]] = i

preorder(0,n-1,0,n-1)