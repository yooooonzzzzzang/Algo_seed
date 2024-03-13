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