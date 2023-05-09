def solution(num_list):
    answer = 1
    for i in num_list:
        if len(num_list) <= 10:
            answer *= i
        else:
            answer += i
    if len(num_list) <= 10:
        return answer
    else:
        return answer - 1