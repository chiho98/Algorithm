import math
def solution(number):
    answer = 0
    for i in number:
        answer += int(i)
        
    return math.floor(answer%9)