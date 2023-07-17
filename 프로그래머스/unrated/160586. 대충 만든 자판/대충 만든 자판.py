def solution(keymap, targets):
    answer = []
    dic = {}
    for i in range(len(keymap)):
        for j in range(len(keymap[i])):
            if dic.get(keymap[i][j]):
                dic[keymap[i][j]] = min(j+1,dic[keymap[i][j]])
            else:
                dic[keymap[i][j]] = j+1
    
    for i in range(len(targets)):
        tmp = 0
        for j in range(len(targets[i])):
            if dic.get(targets[i][j]):
                tmp += int(dic[targets[i][j]])
            else:
                tmp += 100000000
        answer.append(tmp)
    for i in range(len(answer)):
        if answer[i] >= 100000000:
            answer[i] =-1
    return answer        
