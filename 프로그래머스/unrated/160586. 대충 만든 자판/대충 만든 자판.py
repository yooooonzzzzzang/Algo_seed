def solution(keymap, targets):
    answer = []
    dic = {}

    for i in range(len(keymap)):
        for j in range(len(keymap[i])):
            if not dic.get(keymap[i][j]):
                dic[keymap[i][j]] = j+1
            else: dic[keymap[i][j]] = min(j+1, dic[keymap[i][j]])
    for i in targets:
        flag = True
        cnt = 0
        for j in i:
            if not dic.get(j):
                answer.append(-1)
                flag = False
                break
            else: cnt += dic[j]
        if flag == True:
            answer.append(cnt)
    return answer