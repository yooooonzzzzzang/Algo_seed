s = input()
minus = s.split('-')
result = 0
result += sum(map(int,minus[0].split("+")))
for i in range(1, len(minus)):
    result -= sum(map(int, minus[i].split('+')))
print(result)