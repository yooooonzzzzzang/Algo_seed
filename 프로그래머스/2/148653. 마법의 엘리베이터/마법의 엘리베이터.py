def solution(storey):
    ans = 0
    while storey:
        divid = storey % 10
        storey //= 10
        if divid < 5: # 01234
            ans += divid
        else:
            if divid == 5: # 5
                check = storey % 10
                if check > 4:
                    storey += 1
                ans += divid
            else: # 5 보다 클때
                ans += (10-divid)
                storey += 1
    return ans