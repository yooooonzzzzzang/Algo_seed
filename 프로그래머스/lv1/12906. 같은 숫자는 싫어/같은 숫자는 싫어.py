def solution(arr):
    answer = []
    for i in arr:
        if not answer:
            answer.append(i)
        if i != answer[-1]:
            answer.append(i)
            
    return answer