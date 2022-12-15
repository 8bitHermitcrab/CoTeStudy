# 전화번호 목록


# phone_book = ["119", "97674223", "1195524421"]
phone_book = ["123","456","789"]


def solution(phone_book):
    answer = True
    phone_book.sort()

    print(phone_book)

    for i in range(len(phone_book)-1):
        print(f'phone_book[{i}] = {phone_book[i]}')
        print(f'phone_book[{i + 1}][:len(phone_book[{i}])] = {phone_book[i + 1][:len(phone_book[i])]}')
        
        if len(phone_book[i]) < len(phone_book[i+1]):
            if phone_book[i + 1][:len(phone_book[i])] == phone_book[i]:
                answer = False
                break
    return answer

print(solution(phone_book))