def solution(n, s):
    if n>s:
        return [-1]
    else:
        cnt = s // n
        temp = s % n
        answer = [cnt] * n  # 모든 요소를 cnt로 초기화
        for i in range(temp):  
            answer[-(i + 1)] += 1  # 뒤에서부터 1씩 추가
        return answer
