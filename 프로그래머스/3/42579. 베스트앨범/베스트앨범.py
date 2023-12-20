

def solution(genres, plays):
# 속한 노래가 많이 재생된 장르를 먼저 수록합니다.
# 장르 내에서 많이 재생된 노래를 먼저 수록합니다.
# 장르 내에서 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 노래를 먼저 수록합니다.
    answer = []
    dic = dict()
    dic2 = dict() # 재생된 노래수 확인용
    for i in range(len(genres)):
        if genres[i] in dic:
            dic[genres[i]].append([i, plays[i]])
            dic2[genres[i]] += plays[i]
        else: 
            dic[genres[i]] = [[i,plays[i]]]
            dic2[genres[i]] = plays[i]

    for (k, v) in sorted(dic2.items(), key=lambda x:x[1], reverse=True): # 많이 재생된 장르 장렬
        for (i, p) in sorted(dic[k], key=lambda x:x[1], reverse=True)[:2]: # 재생 횟수로 정렬, 두개 슬라이싱
            answer.append(i)

    return answer