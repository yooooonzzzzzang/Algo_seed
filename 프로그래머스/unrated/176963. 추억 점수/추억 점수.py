def solution(name, yearning, photo):
    answer = []
    dic = {}
    for i in range(len(name)):
        dic[name[i]] = yearning[i]
    print(dic)    
    for k in range(len(photo)):
        tmp = 0
        for j in range(len(photo[k])):
            if photo[k][j] in dic:
                tmp += dic[photo[k][j]]
        answer.append(tmp)
    return answer