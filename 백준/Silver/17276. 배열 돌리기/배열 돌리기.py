def _rotate(n, arr):
    # 임시배열 복사해오기
    # 회전하지 않는 원소는 그대로
    tmp = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            tmp[i][j] = arr[i][j]
    # 회전
    for i in range(n):
        # 주 대각선 -> 가운데열
        tmp[i][n//2] = arr[i][i]
        # 가운데 열 (세로) -> 부대각선
        tmp[i][n-1-i] = arr[i][n//2]
        # 부 대각선 -> 가운데 행
        tmp[n//2][i] = arr[n-i-1][i]
        # 가운데 행 (가로) -> 주 대각선
        tmp[i][i] = arr[n//2][i]
    return tmp

for t in range(int(input())):
    n, d = map(int, input().split())
    arr = [list(map(int,input().split())) for _ in range(n)]
    if d > 0:
        d //= 45
    else:
        d = 360 +d
        d //= 45
    # 한꺼번에 띡 바로는 안되고 45도씩 계속 돌려준다
    for _ in range(d):
        arr = _rotate(n,arr)

    # 출력
    for i in range(n):
        for j in range(n):
            print(arr[i][j], end=' ')
        print()