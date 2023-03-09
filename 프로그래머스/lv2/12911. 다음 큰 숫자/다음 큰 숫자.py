def solution(n):
    b = bin(n)
    # 1의 개수 세기
    bcnt1  = b[2:]
    j = bcnt1.count('1')
    for i in range(n+1, 1000001):
        tmp = bin(i)
        tmpcnt1 = tmp[2:]
        if tmpcnt1.count('1') == j:
            break
    answer = int(tmp,2)
    return answer