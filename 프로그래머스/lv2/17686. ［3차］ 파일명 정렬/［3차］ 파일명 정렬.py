
def solution(files):
    answer = []
    arr = []
    for i, file in enumerate(files):
        flag = False
        arr.append([file, "", "", ""])
        tmp = ""
        num = ""
        for char in file:
            if len(num) <= 5 and char.isdigit():
                flag = True
                num += char
            else:
                if flag:
                    break
                tmp += char
        arr[i][1] = tmp
        arr[i][2] = int(num)
        # 대소 비교
        # [1] 사전순비교, 대소문자 구분 x -> 다 소문자로 바꿈
    for i in range(len(arr)):
        arr[i][1] = arr[i][1].lower()

    arr.sort(key=lambda x: (x[1], x[2]))
    for i in range(len(arr)):
        answer.append(arr[i][0])
        print(arr[i][1], arr[i][2])

    return answer
    # [1]이 같으면 [2] 의 숫자 순으로 정렬 (0이 앞에있으면 무시)
    # [1],[2] 가 같을 경우 인덱스 순서로 정렬
