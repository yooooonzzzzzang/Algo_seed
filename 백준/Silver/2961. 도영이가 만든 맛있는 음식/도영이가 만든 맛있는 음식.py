'''
2
3 8
5 8
'''
import sys

input = sys.stdin.readline
n = int(input())
ingre = [list(map(int, input().split())) for _ in range(n)]
def recur(idx, s, b, use):
    global answer
    if idx == n:
        if use == 0:
            return
        result = abs(s-b)
        answer = min(answer, result)
        return
    recur(idx+1, s*ingre[idx][0], b+ingre[idx][1], use+1)
    recur(idx+1, s, b, use)
answer = 9999999999999999999
recur(0,1,0,0)
print(answer)