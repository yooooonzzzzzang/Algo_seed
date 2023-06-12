def solution(babbling):
    can = ["aya", "ye", "woo", "ma"]
    answer = 0
    for i in range(len(babbling)):
        if babbling[i] in can:
            answer += 1
        else:
            for c in can:
                babbling[i] = babbling[i].replace(c,"_")
            k = babbling[i].replace("_","")
            if k =="":
                answer+=1
    return answer