from collections import Counter
def solution(participant, completion):
    arr = list(set(participant) - set(completion))
    if len(arr) == 0 :
        counter = Counter(participant) - Counter(completion)
        for k in counter.elements():
            return k
    else:
        return arr[0]
