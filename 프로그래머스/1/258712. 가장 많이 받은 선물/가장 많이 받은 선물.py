def solution(friends, gifts):
    answer = 0 
    # 받은사람
    get = {i: {j: 0 for j in friends} for i in friends}
    # 준사람
    send = {i: {j: 0 for j in friends} for i in friends}
    # 선물 지수
    degree = {i:0 for i in friends}
    # score
    score = {i:0 for i in friends}
    for gift in gifts:
        s, g = gift.split()
        send[s][g] +=1
        get[g][s] +=1
    # 선물지수 기록
    for i in send:
        tmp = 0
        for j in send[i]:
            tmp += send[i][j]
        for j in get[i]:
            tmp -= get[i][j]
        degree[i] = tmp
    # 계산
    for i in friends:
        for j in friends:
            if i==j:
                continue
            if (send[i][j] ==0 and send[j][i] == 0) or (send[i][j] == send[j][i]):
                if degree[i] > degree[j]:
                    score[i] += 1
            else:
                if send[i][j] > send[j][i]:
                    score[i] += 1
         # 주고 받은 기록이 있을때
            # 더 많이 준 사람이 다음에 선물을 하나 받는다.   
        # 주고 받은 기록이 없거나 기록이 같다면 
            # 선물 지수가 큰 사람이 선물을 하나 받는다. 
                # 선물지수가 같다면 주고 받지 않는다 
    return max(score.values())
