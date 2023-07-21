def solution(ingredient):
    answer = 0
    doma = []
    for i in range(len(ingredient)):
        doma.append(ingredient[i])
        if len(doma) >= 4:
            if doma[-4:] == [1,2,3,1]:
                answer += 1
                # doma = doma[:-4] 슬라이싱 왕 느림 
                del doma[-1]
                del doma[-1]
                del doma[-1]
                del doma[-1]
    return answer