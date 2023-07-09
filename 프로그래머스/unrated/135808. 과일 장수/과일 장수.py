def solution(k, m, score):
    answer = 0
    # k 사과 최대 점수
    # m 한 상자에 들어가는 사과의 수
    # score = arr 
    score.sort(reverse=True)
    for i in range(m-1,len(score)-len(score)%m,m):
        answer += score[i]*m
    #return score[m-1]*m
    return answer