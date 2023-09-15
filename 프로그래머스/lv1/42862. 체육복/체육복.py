def solution(n, lost, reserve):
    answer = 0
    new_lost = list(set(lost) - set(reserve))
    new_reserve = list(set(reserve) - set(lost))

    for i in new_lost:
        if i-1 in new_reserve:
            del new_reserve[new_reserve.index(i-1)]
        elif i+1 in new_reserve:
            del new_reserve[new_reserve.index(i+1)]
        else: answer += 1
            
    return n - answer