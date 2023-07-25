from collections import Counter
def solution(players, callings):
    answer = []
    dic = {value : key for key, value in enumerate(players)}
    # 등수를 딕셔너리에 저장해주고 배열의 인덱스를 직접 바꿔주기 
    for i in callings:
        index = dic[i] 
        dic[i] = index-1
        dic[players[index-1]] += 1
        players[index-1], players[index] = players[index], players[index-1]
    return players
  