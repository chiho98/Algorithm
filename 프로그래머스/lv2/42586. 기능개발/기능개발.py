# 1번째 작업이 완료되지 않으면 2번쨰 작업이 완료되어도 배포 불가능 1번째랑 같이해야함
import math
def solution(progresses, speeds):
    answer = []
    arr = []
    for i in range(len(progresses)):
        arr.append(math.ceil((100-progresses[i])/speeds[i]))
    
    count = 0  # 배포되는 기능의 개수
    max_day = arr[0]  # 현재까지의 최대 배포일

    for i in arr:
        if i > max_day:
            answer.append(count)
            count = 1
            max_day = i
        else:
            count += 1

    answer.append(count)  # 마지막 배포되는 기능 개수 추가
    

    return answer