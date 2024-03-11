def solution(prices):
    answer = [0] * len(prices)
    for i in range(len(prices)-2, -1, -1):
        tmp = 0
        for j in range(i+1,len(prices)):
            if prices[i] <= prices[j]:
                tmp += 1
            else:
                tmp +=1
                break
        answer[i] = tmp
    return answer