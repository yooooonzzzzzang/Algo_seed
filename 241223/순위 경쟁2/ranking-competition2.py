n = int(input())

a, b = 0,0
wins = 'AB' 
cnt = 0

for i in range(n):
    winner, score = input().split()
    if winner =='A':
        a += int(score)
    else:
        b += int(score)
    
    if a > b :
        if wins != 'A':
            wins = 'A'
            cnt +=1 
    elif a == b:
        if wins != 'AB':
            wins = 'AB'
            cnt +=1
    else:
        if wins != 'B':
            wins = 'B'
            cnt += 1
print(cnt)