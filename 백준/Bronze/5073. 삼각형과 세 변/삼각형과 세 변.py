for i in range(1000):
    str = list(map(int, input().split(" ")))
    if str is None or sum(str) == 0:
        break
    else:
        str.sort()
        if str[2] >= str[0] + str[1]:
            print("Invalid")
        elif str[0] == str[1] or str[1] == str[2]:
            if str[0] == str[2]:
                print("Equilateral")
            else:
                print("Isosceles")
        else:
             print("Scalene")
  