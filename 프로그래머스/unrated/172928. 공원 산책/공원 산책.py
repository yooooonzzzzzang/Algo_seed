def solution(park, routes):
    answer = []
    # 동 남 서 북 
    dir = {'E': (0,1), 'S':(1,0),'W':(0,-1), 'N':(-1,0)}
    #'S' 시작, 'X'가 장애물. 'O' 가 지나다니는 길
    
    for i in range(len(park)):
        for j in range(len(park[i])):
            if park[i][j] == 'S':
                for k in range(len(routes)):
                    x,y = i,j
                    d, cnt = routes[k].split()
                    for l in range(int(cnt)):
                        nx, ny = dir[d][0]+i, dir[d][1]+j
                        if 0<= nx< len(park) and 0<= ny < len(park[i]) and park[nx][ny] != "X": 
                            i,j = nx, ny
                        else:
                            i,j = x,y
                            break
                return [i,j]
            '''
            s00
            0xx
            000
            '''
                    
            
    print(park)
    print(routes)
    return answer