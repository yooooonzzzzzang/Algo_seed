from itertools import combinations
N,M = map(int,input().split())
maps = [input().split() for _ in range(N)]
answer = []

'''
1. 치킨집 다 저장
2. 치킨집을 생기게 하면서 - combination? 
3. 치킨거리를 계산하면서 (각 최소가 되어야함) 
4. 모든 가게의 치킨거리를 합한 최솟값
4. 근데 어떻게 브루트포스? 그냥 다 해봐야하는거 아닌가? 제한 조건? 
'''
chickens = []
# 1. 치킨집 다 저장
for i in range(N):
    for j in range(N):
        if maps[i][j] =='2':
            chickens.append((i,j))
# 2. 조합으로 치킨집을 생기게 하면서
def calc(r, c, x,y):
    global house_short
    house_short = min(abs(x-r) + abs(y-c),house_short)


for coordinations in list(combinations(chickens,M)):
    tmp = 0
    for r in range(N):
        for c in range(N):
            if maps[r][c] == '1':
                house_short = 999999999
                for coordi in coordinations:
                    x, y = coordi
                    calc(r,c,x,y)
                tmp += house_short
    answer.append(tmp)
print(min(answer))
