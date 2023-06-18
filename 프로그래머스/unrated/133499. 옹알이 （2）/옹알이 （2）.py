def solution(babbling):
    answer = 0
    can = ["aya","ye","woo","ma"]
    cant = ["ayaaya","yeye","woowoo","mama"]
    
    for i in range(len(babbling)):
        flag= False
        for word in cant:   # 연속해서 같은 발음 체크 
            if word in babbling[i]:
                flag = True
                continue
        if flag == False:   # 아니면 
            if babbling[i] in can:  # 한 단어 일치
                answer += 1
            else:           # 여러 단어 합쳐진
                for c in can:
                    babbling[i] = babbling[i].replace(c,"_")
                k = babbling[i].replace("_","")
                if k =="":
                    answer+=1

    return answer