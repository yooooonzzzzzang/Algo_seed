def solution(genres, plays):
    answer = []
    dic = {}
    for i, v in enumerate(zip(genres, plays)):
        if v[0] not in dic:
            dic[v[0]] = {
                'plays' : {
                    i:v[1]
                },
                'total_play' : v[1]
            }
        else:
            dic[v[0]]['plays'][i] = v[1]
            dic[v[0]]['total_play'] += v[1]
    k = sorted(dic.values(), key =lambda x:-x['total_play'])
    for item in k:
        tmp = sorted(item['plays'].items(), key = lambda x : (-x[1], x[0]))[:2]
        for i in tmp :
            answer.append(i[0])
    return answer