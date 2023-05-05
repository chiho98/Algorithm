def solution(num_list):
    answer = []
    a, b = 0, 0
    for num in num_list:
        if num % 2 == 0:
            a += 1
        elif num % 2 == 1:
            b += 1
    answer = [a, b]
    return answer