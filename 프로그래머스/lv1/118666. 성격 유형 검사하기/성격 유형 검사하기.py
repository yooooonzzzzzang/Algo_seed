def solution(survey, choices):
    answer = ''
    score  = [0,3,2,1,0,1,2,3]
    dic = {"R":0, "T":0, "C":0,"F":0, "J":0,"M":0,"A":0,"N":0}
    for i,v in enumerate(survey):
        check = choices[i]
        if check >=4:
            dic[v[1]] += score[check]
        else:
            dic[v[0]] += score[check]
    arr =[("R","T"),("C","F"),("J","M"),("A","N")]
    for i in arr:
        if dic[i[0]] >= dic[i[1]]:
            answer+=i[0]
        else:
            answer+=i[1]
    return answer
