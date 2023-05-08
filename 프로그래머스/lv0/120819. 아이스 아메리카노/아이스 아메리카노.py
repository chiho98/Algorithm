def solution(money):
    a, b = 0, 0
    a = money // 5500
    b = money - a*5500
    return [a, b]