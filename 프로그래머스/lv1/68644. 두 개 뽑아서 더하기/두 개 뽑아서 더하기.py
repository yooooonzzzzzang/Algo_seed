from itertools import combinations
def solution(numbers):
    answer = []
    k = list(combinations(numbers,2))
    for i in k:
        j = sum(i)
        if j in answer:
            pass
        else:
            answer.append(j)
    
    return sorted(answer)