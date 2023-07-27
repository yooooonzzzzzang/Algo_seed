def solution(food):
    answer = ''
    for i in range(1,len(food)):
        cnt = food[i] // 2 
        answer += str(i) * cnt
    return answer +'0' + answer[::-1]