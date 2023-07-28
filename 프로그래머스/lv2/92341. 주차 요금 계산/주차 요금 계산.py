import math

def solution(fees, records):
    basic_minutes, basic_fee, unit_minutes, unit_fee = fees[0], fees[1], fees[2],fees[3]
    answer =[]
    dic = {}
    dic2 = {}
    for i in records:
        time, car_num, content = i.split()
        # 입차
        if content == "IN":
            dic[car_num]= [time, "23:59"]
        # 출차
        else:
            dic[car_num][1] = time
            # 계산 
            p_h, p_m = map(int, dic[car_num][1].split(":"))
            c_h, c_m = map(int, dic[car_num][0].split(":"))
            total = (p_h*60 + p_m) -(c_h *60 + c_m)
            if car_num in dic2:
                dic2[car_num] += total
            else:
                dic2[car_num] = total
            del dic[car_num]
    for i in dic.keys():
        p_h, p_m = map(int, dic[i][1].split(":"))
        c_h, c_m = map(int, dic[i][0].split(":"))
        total = (p_h*60 + p_m) -(c_h *60 + c_m)
        if i in dic2:
            dic2[i] += total
        else:
            dic2[i] = total
    print(dic2)
    for i in sorted(dic2.keys()):
        total = dic2[i]
        if total > basic_minutes:
            k = math.ceil((total-basic_minutes)/unit_minutes)
            answer.append(basic_fee+k*unit_fee)
        else:
            answer.append(basic_fee)
        
    return answer