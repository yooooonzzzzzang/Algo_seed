arr = list(map(int,input().split()))
for A in range(15):
    for B in range(15):
        for C in range(15):
            for D in range(15):
                if A == B or A == C or A == D or B == C or B== D:
                    continue
                a = arr[A]
                b = arr[B]
                c = arr[C]
                d = arr[D]
                tmp = [a,b,c,d]
                tmp.append(a + b)
                tmp.append(b + c)
                tmp.append(c + d)
                tmp.append(d + a)
                tmp.append(a + c)
                tmp.append(b + d)
                tmp.append(a+ b + c)
                tmp.append(a+ b + d)
                tmp.append(a + c+d)
                tmp.append(b + c + d)
                tmp.append(a+b+c+d) 
                if sorted(tmp) == sorted(arr):
                    print(a,b,c,d)
                    exit(0)