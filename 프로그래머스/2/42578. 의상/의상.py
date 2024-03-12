from itertools import combinations
def solution(clothes):
    dic = dict()
    for i, v in clothes:
        if v not in dic:
            dic[v] = []  
        dic[v].append(i)
    answer = 1
    for i in dic:
        # 사용 안할 경우 +1
        answer *= (len(dic[i]) +1)
    
    # 모두 착용하지 않는 경우 빼주기
    return answer - 1