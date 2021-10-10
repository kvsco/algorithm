#중복이 허락되지않는 자료구조 Set = {} but, 이문제는 중복허용. => list []
sentence = list(map(str,input().split()))
if '' in sentence:
    sentence.remove('')
#print(sentence)
print(len(sentence))


## 입력받는과정에서 split(' ')로 시도했을때 허용X
## 이유=> split() 으로 받으면 공백문자 뛰어쓰기, 탭, 2칸뛰기 등등 모두 하나로 처리
## split(' ') 는 문자열 그대로 스페이스 한칸만 처리해준다.