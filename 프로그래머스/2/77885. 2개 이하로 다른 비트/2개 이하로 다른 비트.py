# bit 로 바꿈
# 01 -> 10 으로 바꾼다
'''
짝수일때는 간단합니다.
짝수를 2진수로 변홨했을때 1의 자리수가 0이기 때문에 +1 해주면 됩니다.
ex) 2 -> 10 -> 11 -> output data : 3
ex) 4 -> 100 -> 101 ->output data : 5
ex) 6 -> 110 -> 111 -> output data : 7

input data가 홀수
input data를 2진수 변환했을때 가장 먼저 나오는 0의 자리를 1로 나머지는 0으로
이 숫자를 input data에 더하고 이 숫자를 /2 한 값을 빼주시면 됩니다.
ex) 5 -> 101 -> 가장 먼저 나오는 0을 탐색(2의 1승자리) -> 101 + 10 - 1 -> 110 ->output data : 6
ex) 3 -> 11 -> 가장 먼저 나오는 0을 탐색(2의 2승자리) -> 11 + 100 - 10 -> 101 ->output data : 5


'''
def solution(numbers):
    answer = []
    for n in numbers:
        if n % 2 == 0:
            answer.append(n+1)
            continue
        else:
            n_bin = '0' + (bin(n)[2:])
            n_bin =  n_bin[:n_bin.rindex('0')] + '10' + n_bin[n_bin.rindex('0')+2 : ]
            answer.append(int(n_bin,2))
                
    return answer