def solution(s, n):
    answer = ''
    lower_alph = 'abcdefghijklmnopqrstuvwxyz'
    upper_alph = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    for i in s:
        if i.islower():
            answer += lower_alph[(lower_alph.index(i)+n)%26]
        elif i.isupper():
            answer += upper_alph[(upper_alph.index(i)+n)%26]
        else:
            answer += i
    return answer