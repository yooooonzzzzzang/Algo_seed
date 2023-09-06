# 상,하,좌,우 
dx = [1,-1, 0, 0]
dy = [0, 0, 1, -1]
def check_student(x,y):
    for k in range(4):
        nx, ny = dx[k]+x, dy[k]+y
        # 직선으로 쭉쭉 확인 장애물 나오면 끝
        while 0<=nx<N and 0<=ny<N and maps[nx][ny] != 'O':
            if maps[nx][ny] == 'S':  # 학생 잡음
                return True
            else: # 직선으로 계속 확인
                nx += dx[k]
                ny += dy[k]
    return False # 학생 못잡음



def solution(cnt):
    global answer
    if cnt == 3:
        miss_cnt = 0
        for i in range(N):
            for j in range(N):
                # 선생님 돌아다니기
                # 학생 확인
                if maps[i][j] == 'T':
                    if not check_student(i,j):
                        miss_cnt += 1
        # print(miss_cnt,teacher_cnt)
        # 모든 선생님이 다 놓치면 성공
        if miss_cnt == teacher_cnt:
            answer = True
        return

    for i in range(N):
        for j in range(N):
            if maps[i][j] == 'X':
                maps[i][j] = 'O'
                cnt += 1
                solution(cnt)
                maps[i][j] = 'X'
                cnt -= 1
N = int(input())
maps = [input().split() for _ in range(N)]
teacher_cnt = 0
# 선생님 수 세기
for map in maps:
    teacher_cnt += map.count('T')
answer = False

solution(0)
print('YES') if answer else print('NO')