def solution(phone_book):
    answer = True
    phone_book.sort()

    for i, j in zip(phone_book, phone_book[1:]):
        if j.startswith(i):
            return False
    # 뒤에가 (j) 앞의(i)번호로 시작하는 번호면

    return answer