def solution(d, budget):
    answer = 0
    d.sort()
    tmp = 0
    for i in range(len(d)):
        tmp += d[i]
        answer += 1
        if tmp > budget:
            return answer-1
    return answer