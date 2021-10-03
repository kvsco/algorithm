def solution(board, moves):
    answer = 0
    
    board.reverse()
    N = len(board)
    n_board = []
    #각각의 열 별로 stack구성.
    for i in range(N):
        temp = []
        temp2 = []
        for j in range(N):
            temp.append(board[j][i])
        
        for t in temp :
            if t > 0 :
                temp2.append(t)
        #print(temp2)
        n_board.append(temp2)
    
    basket = []
    nxt = None
    #인형뽑기
    for m in moves :
        m = m-1
        if not n_board[m] : # 빈 줄이라면
            continue
        else : # 열려있으면
            nxt = n_board[m].pop()
        
        if len(basket) >0 :
            lst = basket.pop()
            if lst == nxt :
                answer +=2
            else :
                basket.append(lst)
                basket.append(nxt)
        else :
            basket.append(nxt)
    return answer