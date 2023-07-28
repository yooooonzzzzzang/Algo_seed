def solution(fees, records):
    basic_minutes, basic_fee, unit_minutes, unit_fee = fees[0], fees[1], fees[2],fees[3]
    dic = {}
    cars =[]
    for i in records:
        time, car_num, content = i.split()
        cars.append(car_num)
        # 입차
        if content == "IN":
            dic[car_num] = [time, "23:59"]
        # 출차
        else:
            dic[car_num][1] = time
            
    print(dic)
    answer = []
    # 기본 시간 이하면 기본요금, 초과시 단위시간마다 단위요금 청구 
    # 초과시간이 나눠지지 않으면 올림
    # 차량번호가 작은 자동차부터 주차요금 계산 하기 
    for i in sorted(dic.keys()):
        print(dic[i])
        p_h, p_m = map(int, dic[i][1].split(":"))
        c_h, c_m = map(int, dic[i][0].split(":"))
        total = (p_h*60 + p_m) -(c_h *60 + c_m)
        if total > basic_minutes:
            pass
        else:
            answer.append(basic_fee)
    return answer