def solution(data, ext, val_ext, sort_by):
    answer = []
    # data ["코드 번호(code)", "제조일(date)", "최대 수량(maximum)", "현재 수량(remain)"]
    #  "제조일이 20300501 이전인 물건들을 현재 수량이 적은 순서"
    dic = {"code":0, "date":1, "maximum":2, "remain":3}
    for i in data:
        if i[dic[ext]] < val_ext:
            answer.append(i)
    answer.sort(key = lambda x: x[dic[sort_by]])
    return answer