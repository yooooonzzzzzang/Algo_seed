def solution(brown, yellow):
    answer = [0,0]
    s = yellow + brown                # 전체 면적
    for i in range(s-1, 0, -1):
        if s % i:
            pass
        height = s // i;
        y = (i -2) * (height -2)
        b = s - y
        if y == yellow and b == brown:
            answer[0] = i
            answer[1] = height
            break
    return answer