def solution(today, terms, privacies):
    answer =[]
    policy = {key:value for key,value in map(str.split,terms)}
    today = list(map(int, today.split(".")))
    todays = (today[0]-1)*12*28 + (today[1]-1)*28 + today[2]
    
    for i in range(len(privacies)):
        tmp, month = privacies[i].split()
        check_day = list(map(int, tmp.split(".")))
        check_days = (check_day[0]-1)*12*28 + (check_day[1]-1)*28 + check_day[2]
        if todays >= (check_days + (int(policy[month]) * 28)):
            answer.append(i+1)
        
    return answer