a, b = input().split()

a = int(a[::-1]) # 문자열 뒤집기
b = int(b[::-1])
[print(a) if a>b else print(b)] #함축 그냥한번써봄..ㅎ

