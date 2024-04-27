from itertools import combinations
import copy
def solution(relation):
    n = len(relation)
    col_n = len(relation[0])
    # 1. 조합구하기 - 속성idx 의 모든 조합 = col_combi
    col_combi = []
    for i in range(1,col_n+1):
        for j in list(combinations(range(col_n,), i)):
            col_combi.append(j)
    # 2. 유일성 판별 = unique 
    unique = set()
    for cols in col_combi:
        tmp = set()
    
        for row in range(n):
            str_s =""
            for col in cols:
                str_s += relation[row][col]
            tmp.add(str_s)
        if len(tmp) == n:
            unique.add(cols)
            
    # 3. 최소성 판별 -> 한 속성을 뺐을때 식별이 된다면 후보키가 아니다. = unique_c
 
    unique = sorted(unique, key=lambda x: len(x))
    unique= list(unique)
    unique_c = copy.deepcopy(unique)
            
    for i in range(len(unique)):
        for j in range(i+1,len(unique)):
            key1 = set(unique[i])
            key2 = set(unique[j])
            if key1.issubset(key2):
                try:
                    unique_c.remove(tuple(key2))
                except:
                    continue
 

                
                        
                
    return len(unique_c)
