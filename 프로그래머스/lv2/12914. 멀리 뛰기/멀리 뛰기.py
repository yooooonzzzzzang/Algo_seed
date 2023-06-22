def solution(n):
    answer = 1
    # 1칸 씩 뛰는 방법 + 1 해줘야함
    # 2를 나눠서 몫과 나머지를 내고 아마 몫 n 이면 나머지 1이나 0 일것
    mok = n //2
    na = n % 2
    for i in range(mok):
        for j in range(i, -1,-1):
            print(j)
    
    mok = n//2
    na = n % 2 
    return answer