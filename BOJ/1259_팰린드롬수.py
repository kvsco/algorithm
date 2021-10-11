while True:
    n = input()
    pal = n[::-1]
    if n == '0' :
        break
    if n == pal:
        print('yes')
    else:
        print('no')

    