def solution(my_string):
    answer = 0
    numbers = ''.join(filter(str.isdigit, my_string))
    numbers = list(numbers)
    for i in numbers:
        answer += int(i)
    return answer