def solution(word):
    arr = ['A','E','I','O','U']
    cnt = 0
    answ = 0
    def dfs(tmp):
        nonlocal cnt
        nonlocal answ
        if len(tmp) > 5:
            return 
        cnt += 1
        if tmp == word:
            answ = cnt
        
        for i in arr:
            dfs(tmp + i)
                
    dfs('')
    return answ-1         

'''
from itertools import product
def solution(word):
    answer = 0
    arr = ['A','E','I','O','U']
    tmp = []
    for i in range(1, 6):
        for k in list(product(arr, repeat = i)):
            tmp.append(''.join(k))
    tmp.sort()
    
    return tmp.index(word) + 1
'''