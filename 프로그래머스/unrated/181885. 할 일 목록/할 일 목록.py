def solution(todo_list, finished):
    answer = []
    for i in range(len(todo_list)):
        print(finished[i])
        if finished[i] == False:
            answer.append(todo_list[i])
    return answer