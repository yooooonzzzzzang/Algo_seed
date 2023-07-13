def solution(N, stages):
    people = len(stages)
    answer = {}
    for i in range(1,N+1):
        if people != 0:
            not_clear = stages.count(i)
            answer[i] = not_clear/people
            people -= not_clear
        else:
            answer[i] = 0
    
    return sorted(answer, key=lambda x:answer[x], reverse=True)