def solution(a,b,n):
    answer = 0
    # a: 빈 병의 개수를 가져다 주면
    # b: 개의 콜라병을 주는 마트가 있을떄
    # n: 개를 가져다주면 몇 병을 받을 수 있는지
    while n >= a:
        mok = n // a  # 몫
        na = n % a    # 나머지
        answer += mok * b 
        n = na + mok * b
    return answer