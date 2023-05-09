def solution(my_string, alp):
    answer = ''
    for i in my_string:
        if i == alp:
            print(i)
            answer += i.upper()
        elif i != alp:
            answer += i
    return answer