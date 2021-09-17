#-*- coding:utf-8 -*-

def solution1(participant, completion):
    answer = ''
    
    for i in completion :
        if i in participant :
            participant.remove(i)
    answer = participant
    return answer[0]
'''
** 문제는 해결되지만, 시간복잡도가 높은이유

in => 이 한줄이지만. 이 연산이 복잡도가 participant 길이만큼 발생
   => in이 for문 한줄을 더 돌린거랑 똑같다.
그래서 느리다 n 제곱만큼의 시간이 든다.
10만이니깐 해당 코드를 돌리면 최대 10만*10만 만큼 시간복잡도 높아짐

이제 이걸 개선.
코딩테스트 시험형으로 보는건 이걸 물어보는문제. + 구현 잘하냐

n^2, n^3 ->nlogn ,n, n^2, n^2logn
'''
#해시로 개선된 코드

def solution2(participant, completion):
    
    P={}
    
    for i in participant :
        P[i]=0
    
    for i in participant :
        P[i]+=1
        
    for i in completion :
        P[i]-=1
    
    for i in P :
        if P[i]==1 :
            return i
         
'''

N 이다. 4*N

앞에서 10만 개들어오면

앞에코드론 10만*10만 하는데

아래거는 10만 *4 연산.

이런식으로 메모리에 필요한값을 미리 기억시켜요 기억 시켜서 순회하는 양을 줄이는거야.

포문 하나 돌면 그 데이터 길이만큼 복잡도 발생

따로 놀면 더한다

겹겹이 들어가면 곱한다.


for 
    for 이렇게 들어가면 곱하기


'''
