def solution(s):
    answer = []
    # 글자의 왼쪽으로 같은 글자가 있는지 확인
    for i in range(len(s)):
        for j in range(i-1,-1,-1):
            if s[i] == s[j]:
                answer.append(i-j)
                break
        else:
            answer.append(-1)
    return answer