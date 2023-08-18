def solution(s):
    # 이진변환 횟수, 제거된 0 의 개수
    answer = [0,0]
    print(s.count('0'))
    while s != '1':
        scount = s.count('0')
        answer[1] += scount
        s = bin(len(s)-scount)[2:]
        answer[0] += 1
            # 0 제거 하고 cnt 길이를 2진법으로 변경 
    return answer