def solution(num_list):
    answer = 1
    answer2 = sum(num_list) **2
    for i in num_list:
        answer *= i
    if answer > answer2:
        return 0
    else:
        return 1