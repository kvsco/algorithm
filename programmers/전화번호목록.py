def solution(phone_book):
    answer = True

    p = {}
    for i in phone_book:
        p[i] = 1
    # 딕셔너리로 자료구조 변환하여 해시 기능사용.
    for i in phone_book:
        check = ''

        for j in i:
            check += j
            #해당 번호를 문자별로 하나씩 붙여가며 딕셔너리 key로 존재하는지 찾음.
            #해당 접두번호 ( check ) 가 현재 번호 (i) 가 아닐때 answer return하겠다.
            if check in p and check != i:
                return False