def solution(my_string, num1, num2):
    arr = list(my_string)
    print(arr)
    arr[num1] = my_string[num2]
    arr[num2] = my_string[num1]
    
    return "".join(map(str, arr))