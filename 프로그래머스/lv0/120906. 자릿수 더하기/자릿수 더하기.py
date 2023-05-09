def solution(n):
    n = str(n)
    n = list(n)
    answer = 0
    for i in n:
        answer += int(i)
    return answer