for _ in range(int(input())):
    tmp = 1
    n, r = map(int, input().split())
    if n==r :
        print(1)

    else:
        tmp = n
        temp = 1
        tempo = r
        while tmp != 0:
            temp *= tempo
            tmp -=1
            tempo -= 1

        tmp2 = n
        temp2 = 1
        while tmp2 != 0:
            temp2 *= tmp2
            tmp2 -=1
        print(temp//temp2)