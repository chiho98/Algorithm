def solution(my_strings, parts):
    answer = ''
    for i in range(len(my_strings)):
        strings = my_strings[i]
        a = parts[i][0]
        b = parts[i][1]
        answer += strings[a:b+1]
    return answer