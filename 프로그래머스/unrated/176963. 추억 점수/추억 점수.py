def solution(name, yearning, photo):
    answer = []
    dic = { key : value for key,value in zip(name, yearning)}
    print(dic)
    for i in range(len(photo)):
        tmp = 0
        for j in range(len(photo[i])):
            if photo[i][j] in dic.keys():
                tmp += dic[photo[i][j]]
        answer.append(tmp)
    return answer