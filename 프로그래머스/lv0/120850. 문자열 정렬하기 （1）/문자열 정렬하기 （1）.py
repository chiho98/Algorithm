def solution(my_string):
    answer = []
    my_string = list(my_string)
    my_string.sort()
    for i in my_string:
        if i in str([0,1,2,3,4,5,6,7,8,9]):
            answer.append(i)
    return list(map(int, answer))