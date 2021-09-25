def solution(clothes):
    answer = 0

    c = {}
    # 딕셔너리 초기화
    for i in clothes:
        c[i[1]] = 0

    for i in clothes:
        c[i[1]] += 1
    # 입을수 있는 의상을 분류

    if len(c) == 1:
        return list(c.values())[-1]
    else:
        # print(c)
        num_clo = []
        for i in c:
            num_clo.append(c[i])

        c_sum = 0
        multi = 1
        for i in num_clo:
            # 하나씩입는경우
            c_sum += i
            multi *= i
        return c_sum * multi - 1