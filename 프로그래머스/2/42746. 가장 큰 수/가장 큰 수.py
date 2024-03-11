def solution(numbers):
    answer = ""
    num = list(map(str, numbers))
    # 문자는 앞에서부터 차례차례 큰 수인지 비교 (자리 상관없음)
    num.sort(key=lambda x: x * 3, reverse=True)
    for i in num:
        answer += str(i)
    if answer[0] =='0':
        return '0'
    return answer