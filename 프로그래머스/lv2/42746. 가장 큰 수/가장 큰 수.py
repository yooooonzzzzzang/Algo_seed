def solution(num):
    num = list(map(str, num))
    num.sort(key=lambda x: x * 3, reverse=True)
    answer = ''.join(num)
    if answer[0] =='0':
        return '0'
    return answer