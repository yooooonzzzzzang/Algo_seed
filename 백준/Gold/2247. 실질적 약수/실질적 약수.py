def csod(n):
    answer = 0
    i =2
    while i <= n//2:
        k = n//i
        b = n//k
        c = (k-1) * (b -i+1)*(i+b)//2
        answer = (answer + c) % 1000000
        i = b+1
    return answer

n= int(input())
print(csod(n))