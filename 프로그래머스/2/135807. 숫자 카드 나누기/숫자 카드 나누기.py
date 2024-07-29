def solution(arrayA, arrayB):
    answer = [0]
    # 각자 최대 공약수를 구해서 상대의 수와 나눠지는 지 확인
    # 각자 최대 공약수를 구해서 상대의 수와 나눠지는 지 확인
    
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    def list_gcd(numbers):
        current_gcd = numbers[0]
        for num in numbers[1:]:
            current_gcd = gcd(current_gcd, num)
        return current_gcd
    gcd_A = list_gcd(arrayA)
    gcd_B = list_gcd(arrayB)
    flag = False
    for i in arrayB:
        if i % gcd_A == 0:
            flag = True
    if not flag: answer.append(gcd_A)
    flag = False
    for i in arrayA:
        if i % gcd_B == 0:
            flag = True
    if not flag : answer.append(gcd_B)
    return max(answer)