def solution(t, p):
    answer = 0
    a = len(p)-1
    for i in range(len(t)):
        if len(t[i:i+a+1]) == len(p):
            if t[i:i+a+1] <= p:
                answer += 1
        # if int(t[i:i+a]) <= int(p):
            # answer += 1
    return answer