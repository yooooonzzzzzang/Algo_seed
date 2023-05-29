n = int(input())
alphabet ="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
frequency = [0] * 26 

for i in range(n):
  enter = input() 
  weight=1 #가중치 초기값은 1
  
  for j in enter[::-1]:
    frequency[alphabet.find(j)] += weight
    weight *= 10 #자리수가 하나 올라갈때마다 가중치를 10 씩 곱해준다 
frequency.sort(reverse = True)
total = 0 

for i in range(9,0,-1):
  total = total + (frequency[9-i] * i)
print(total)
