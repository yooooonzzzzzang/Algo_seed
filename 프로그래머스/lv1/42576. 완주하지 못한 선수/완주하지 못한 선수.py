from collections import Counter
def solution(participant, completion):
    com_c = Counter(completion)
    par_c = Counter(participant)
    # 동명이인이 있는 경우와 par 에는 있는데 com에는 없는 경우
    for name in participant:
        if par_c.get(name) != com_c.get(name) or not com_c.get(name):
            return name