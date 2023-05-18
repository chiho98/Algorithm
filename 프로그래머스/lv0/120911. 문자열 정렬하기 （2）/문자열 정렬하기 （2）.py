def solution(my_string):
    answer = ''
    my_string2 = list(my_string.lower())
    my_string2.sort()
    print(my_string2)
    for i in my_string2:
        answer += i
    
    
    return answer