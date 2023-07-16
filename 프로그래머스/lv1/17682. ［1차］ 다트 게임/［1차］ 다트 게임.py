def solution(dartResult):
    answer = []
    # 1. 일단 3개로 나눠보자 10 어케 할겨????  -> replace('10','A') 
    n = ''
    for i in dartResult:
        if i.isnumeric():
                n += i
        elif i== 'S':
            n = int(n)
            answer.append(n)
            n = ''
        elif i == 'D':
            n = int(n)**2
            answer.append(n)
            n = ''
        elif i == 'T':
            n = int(n)**3
            answer.append(n)
            n = ''
        elif i == '*':
            if len(answer) > 1:
                answer[-2] *= 2
                answer[-1] *= 2
            else:
                answer[0] *= 2

        elif i == '#':
            answer[-1] *= -1

    return sum(answer)