# 변수 선언 및 입력:
n = int(input())
bomb_type = [
    [0 for _ in range(n)]
    for _ in range(n)
]
bombed = [
    [False for _ in range(n)]
    for _ in range(n)
]

ans = 0

bomb_pos = list()


def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n


def bomb(x, y, b_type):
    # 폭탄 종류마다 터질 위치를 미리 정의합니다.
    bomb_shapes = [
        [],
        [[-2, 0], [-1, 0], [0, 0], [1, 0], [2, 0]],
        [[-1, 0], [1, 0], [0, 0], [0, -1], [0, 1]],
        [[-1, -1], [-1, 1], [0, 0], [1, -1], [1, 1]]
    ]
    
    # 격자 내 칸에 대해서만 영역을 표시합니다.
    for i in range(5):
        dx, dy = bomb_shapes[b_type][i];
        nx, ny = x + dx, y + dy
        if in_range(nx, ny):
            bombed[nx][ny] = True

            
def calc():
    # Step1. 폭탄이 터진 위치를 표시하는 배열을
    # 초기화합니다.
    for i in range(n):
        for j in range(n):
            bombed[i][j] = False
            
    # Step2. 각 폭탄의 타입에 따라 
    # 초토화 되는 영역을 표시합니다.
    for i in range(n):
        for j in range(n):
            if bomb_type[i][j]:
                bomb(i, j, bomb_type[i][j])
	
    # Step3. 초토화된 영역의 수를 구합니다.
    cnt = 0
    for i in range(n):
        for j in range(n):
            if bombed[i][j]:
                cnt += 1
    
    return cnt


def find_max_area(cnt):
    global ans
    
    if cnt == len(bomb_pos):
        ans = max(ans, calc())
        return

    for i in range(1, 4):
        x, y = bomb_pos[cnt]
        
        bomb_type[x][y] = i
        find_max_area(cnt + 1)
        bomb_type[x][y] = 0


for i in range(n):
    given_row = list(map(int, input().split()))
    for j, bomb_place in enumerate(given_row):
        if bomb_place:
            bomb_pos.append((i, j))

find_max_area(0)

print(ans)
