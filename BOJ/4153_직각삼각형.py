while True:
    a,b,c = map(int,input().split())

    if a==0 and b==0 and c==0 :
        break
    triangle = [a,b,c]
    triangle = sorted(triangle) # 순서대로 정렬 마지막 수 = 빗변.
    
    f = triangle[0]**2
    s = triangle[1]**2
    t = triangle[2]**2

    if f+s == t :
        print('right')
    else:
        print('wrong')

    