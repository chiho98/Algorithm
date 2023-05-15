def solution(answers):
    answer = []
    
    # 수포자들의 찍기 패턴
    pattern_1 = [1, 2, 3, 4, 5]
    pattern_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    pattern_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    # 수포자들의 정답 개수를 저장할 리스트
    scores = [0, 0, 0]
    
    # 정답 확인 및 점수 계산
    for i in range(len(answers)):
        if answers[i] == pattern_1[i % len(pattern_1)]:
            scores[0] += 1
        if answers[i] == pattern_2[i % len(pattern_2)]:
            scores[1] += 1
        if answers[i] == pattern_3[i % len(pattern_3)]:
            scores[2] += 1
    
    # 가장 많은 문제를 맞힌 사람 찾기
    max_score = max(scores)
    for i in range(len(scores)):
        if scores[i] == max_score:
            answer.append(i + 1)
    
    return answer