# 영영소 4 개 & 가격
# 각 영양분의 합 최소 / 가격은 최소
# 만족하는 것이 여러가지일때 사전순으로 빠른것
# 조건 만족 x -1 출력
'''
6
100 70 90 10
30 55 10 8 100
60 10 10 2 70
10 80 50 0 50
40 30 30 8 60
60 10 70 2 120
20 70 50 4 4
'''
n = int(input())
mp, mf,ms,mv = map(int,input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
answer = 1e9
answer_used =[]
used = []
def recur(idx, p, f, s, v, total):
    global answer
    global answer_used
    global used
  
    if p >=mp and f >=mf and s >= ms and v >= mv:
        if answer > total:
            answer = min(answer, total)
            answer_used = []
            for i in used:
                answer_used.append(i)
    if idx == n:
        return
    used.append(idx+1)
    recur(idx+1, p+arr[idx][0], f+arr[idx][1], s+arr[idx][2], v+arr[idx][3], total+arr[idx][4])
    used.pop()
    recur(idx+1, p,f,s,v,total)
recur(0,0,0,0,0,0)

answer_used.sort()
if answer_used:
    print(answer)
    print(*answer_used)
else:
    print(-1)