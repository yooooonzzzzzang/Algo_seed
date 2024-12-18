'''
1. 처음 시작이 ABC인 경우에는 교환 없이 정렬이 가능하다.
2. 처음 시작에 ACB처럼 오직 1명만 원하는 자리에 위치하는 경우라면, 1번의 교환으로 정렬이 가능하다.
3. 처음 시작에 CAB처럼 아무도 원하는 자리에 위치하지 않는 경우라면, 2번의 교환으로 정렬이 가능하다.
'''
data = list(map(int, input().split()))

if data[0] + 1 == data[1] and data[1] + 1 == data[2]:
    print(0)

elif data[0] + 2 == data[1] or data[1] + 2 == data[2]:
    print(1)
    
else:
    print(2)