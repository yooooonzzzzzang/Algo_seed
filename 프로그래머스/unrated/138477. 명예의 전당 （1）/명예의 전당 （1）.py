def solution(k, score):
    answer = []
    q = []
    for i in range(len(score)):
        # q가 없을때  , 자리가 남아있을때 -> 추가
        if not q or (len(q)> 0 and len(q) < k):
            q.append(score[i])
            if len(q) == k:
                answer.append(min(q))
                continue
        # q 길이가 다 찼지만  
        if len(q) >= k and score[i] >= min(q):
            q.remove(min(q))
            q.append(score[i])
        answer.append(min(q))
    return answer