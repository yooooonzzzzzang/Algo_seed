def solution(id_list, report, k):
    answer = [0] * len(id_list)
    # 딕셔너리 value를 set 으로 이름 넣고
    # length 
    # id 순서대로 
    dic = {}
    for i in range(len(report)):
        a, b = report[i].split()
        if b in dic:
            dic[b].add(a)
        else:
            dic[b] = set()
            dic[b].add(a)
    for key, value in dic.items():
        if len(value) >= k:
            for i in value:
                answer[id_list.index(i)]+= 1
    return answer