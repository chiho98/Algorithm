def solution(myString):
    arr = "abcdefghijk"
    answer = ''
    for i in myString:
        # print(i)
        if i in arr:
            answer += "l"
        else:
            answer += i
    
    return answer