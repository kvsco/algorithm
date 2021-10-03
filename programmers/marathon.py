def solution1(participant, completion):
    answer = ''

    for i in completion:
        if i in participant:
            participant.remove(i)
    answer = participant
    print(answer)
    return answer[-1]

print( solution1(['a','b','c'],['a','c']) )