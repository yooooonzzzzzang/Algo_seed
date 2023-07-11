def div_n(n):
    divisorsList = []
    for i in range(1, int(n**(1/2)) + 1):
        if (n % i == 0):
            divisorsList.append(i) 
            if ( (i**2) != n) : 
                divisorsList.append(n // i)
    return len(divisorsList)

def solution(number, limit, power):
    arr = []
    for n in range(1, number+1):
        arr.append(div_n(n))
    for i in range(len(arr)):
        if arr[i] >limit:
            arr[i] = power        
    return sum(arr)