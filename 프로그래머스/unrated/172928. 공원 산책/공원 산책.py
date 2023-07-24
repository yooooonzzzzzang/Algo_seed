def solution(park, routes):
    answer = []
    # 동 남 서 북 
    dir = {'E': (0,1), 'S':(1,0),'W':(0,-1), 'N':(-1,0)}
    
    for i in range(len(park)):
        for j in range(len(park[i])):
            # 시작점 찾아서 시작! 
            if park[i][j] == 'S':
                for k in range(len(routes)):
                    # 나중 예외처리를 위해
                    x,y = i,j
                    d, cnt = routes[k].split()
                    # 거리만큼 반복
                    for l in range(int(cnt)):
                        nx, ny = dir[d][0]+i, dir[d][1]+j
                        # 조건 부합 -> 방향으로 1거리씩 이동
                        if 0<= nx< len(park) and 0<= ny < len(park[i]) and park[nx][ny] != "X": 
                            i,j = nx, ny
                        # 중간에 잘못된 경우, 이전으로 되돌리고 종료
                        else:
                            i,j = x,y
                            break
                return [i,j]
                    
