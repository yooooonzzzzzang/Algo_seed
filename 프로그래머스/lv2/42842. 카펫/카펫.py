def solution(brown, yellow):
    answer = []
    # 방법1) 이 둘을 더한 직사각형을 먼저 구해서 될 수 있는 가로 세로를 전부 검증하는 방법 
    total = brown + yellow
    # 약수 구해주기 (가로 >= 세로)
    divisor = []
    for i in range(1,total//2+1):
        mok = total // i
        na = total % i
        if na == 0 and mok >= i:
            divisor.append([mok , i])
    # 가로 -2 * 세로 -2 == yellow: 정답
    for width, height in divisor:
        if (width-2) * (height -2) == yellow:
            return [width, height]