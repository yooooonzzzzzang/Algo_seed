def solution(s):
    temp = ''
    for i in range(len(s)):
        temp += s[i].lower()
    answer = ''
    answer+= temp[0].upper()
    for i in range(1,len(temp)):
        if temp[i-1] == ' ' and temp[i].islower() == True:
            answer += temp[i].upper()
        else:
            answer += temp[i]

    return answer