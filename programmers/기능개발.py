from collections import deque

def solution(progresses, speeds):
    answer =[]
    p = deque(progresses)
    s = deque(speeds)
    day = 0
    result = 0
    
    while len(p) > 0 :
        if p[0] + (s[0] * day) >= 100 :
            result += 1
            p.popleft()
            s.popleft()
            
        else :
            if result > 0:
                answer.append(result)
                result = 0
            day += 1
    #마지막 result
    answer.append(result)
    
    return answer

print( solution( [], [] ))