n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
bombs = []
bomb_shapes = [
    [[-2, 0], [-1, 0], [0, 0], [1, 0], [2, 0]],
    [[-1, 0], [1, 0], [0, 0], [0, -1], [0, 1]],
    [[-1, -1], [-1, 1], [0, 0], [1, -1], [1, 1]]
]

def bomb(x, y, type_bomb, new_arr):
    for i in range(5):
        dx, dy = bomb_shapes[type_bomb][i]
        nx = x + dx
        ny = y + dy
        if 0 <= nx < n and 0 <= ny < n:
            new_arr[nx][ny] = 1

def init():
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1:
                bombs.append([i, j])

def exploded(arr):
    new_arr = [[0] * n for _ in range(n)]
    cnt = 0
    for (x, y), types in zip(bombs, arr):
        bomb(x, y, types, new_arr)
    for i in range(n):
        for j in range(n):
            if new_arr[i][j] == 1:
                cnt += 1
    return cnt

def recur(arr, max_area):
    # 최적화: 현재 폭탄 배열을 완성하고 계산을 바로 하도록 합니다.
    if len(arr) == len(bombs):
        return max(max_area, exploded(arr))
    
    best_area = max_area  # 현재까지의 최고값을 기억
    for i in range(3):
        arr.append(i)
        best_area = recur(arr, best_area)
        arr.pop()
    
    return best_area

# 초기 설정 및 재귀 탐색 시작
bombs = []
init()
ans = recur([], 0)
print(ans)
