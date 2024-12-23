n = int(input())

a, b, c = 0,0,0
wins = 'ABC' 
cnt = 0

for i in range(n):
    winner, score = input().split()
    if winner =='A':
        a += int(score)
    elif winner =='B':
        b += int(score)
    else:
        c += int(score)
    # a b c ab bc ac abc    
    if a > b and a > c:
        if wins != 'A':
            wins = 'A'
            cnt +=1 
    elif b > a and b > c :
        if wins != 'B':
            wins = 'B'
            cnt += 1
    elif c > a and c >b :
        if wins != 'C':
            wins = 'C'
            cnt += 1
    elif a == b and b > c:
        if wins != 'AB':
            wins = 'AB'
            cnt +=1
    elif b== c and c > a:
        if wins != 'BC':
            wins = 'BC'
            cnt +=1
    elif a== c and a > b:
        if wins != 'AC':
            wins = 'AC'
            cnt +=1
    else:
        if wins != 'ABC':
            wins = 'ABC'
            cnt += 1
print(cnt)