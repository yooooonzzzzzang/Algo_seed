def solution(brown, yellow):
    answer = []
    area = brown + yellow
    for i in range(3, int(area**0.5)+1):
        # 세로, 가로
        if area % i ==0:
            w = (i*2) + (area//i * 2) - 4 
            h = area- w
            if w == brown and h == yellow:
                # if i % 2 == 0 and (area//i) % 2 == 0: 
                return [area//i, i]
