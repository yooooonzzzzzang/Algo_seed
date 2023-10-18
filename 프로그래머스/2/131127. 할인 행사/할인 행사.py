from collections import Counter
def solution(want, number, discount):
    answer = 0
    discount_days = len(discount)
    buy = {key: value for key, value in zip(want, number)}
    
    # discount 를 10 씩 점점 늘려서 cnt 랑 비교 같으면 +=1
    # struggle : 배열을 전체 생성 보다 맨 앞거 빼주고 뒤에거 더해줘서 메모리 사용 줄이고 싶음
    for i in range(discount_days):
        dis_counter = Counter(discount[i:i+10])
        a = 0
        for key, value in buy.items():
            if value - dis_counter[key] > 0:
                continue
            a += 1
        if a == len(want):
            answer +=1
    # buy = {key: value for key, value in zip(want, number)}
    return answer