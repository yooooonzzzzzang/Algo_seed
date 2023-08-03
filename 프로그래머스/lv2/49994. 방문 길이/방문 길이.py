def solution(dirs):
    dir = {'U':(1,0),'D':(-1,0),'R':(0,1),'L':(0,-1)}
    answer = 0
    # 좌표평면의 범위 -5~5 넘어가면 무시
    # 이동
    x,y = 0,0
    cnt = set()
    for i in range(len(dirs)):
        nx = dir[dirs[i]][0] + x
        ny = dir[dirs[i]][1] + y
        if -5<=nx<=5 and -5<=ny<=5 :
            cnt.add(((x,y),(nx,ny)))
            cnt.add(((nx,ny),(x,y)))
            x,y = nx,ny
    # 중복체크
    print(cnt)
    # 처음 걸었던 길만 cnt-set?
    return len(cnt)//2