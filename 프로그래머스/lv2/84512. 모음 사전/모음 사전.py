from itertools import product
def solution(word):
    answer = 0
    arr =['A','E','I','O','U']
    k = []
    for i in range(1,6):
        k.append(list(product(arr, repeat=i)))
    tmp = []
    for i in k:
        for j in i:
            tmp.append(j)
    tmp.sort()
    answer = []
    for k in tmp:
        answer.append(''.join(k))
    return answer.index(word)+1