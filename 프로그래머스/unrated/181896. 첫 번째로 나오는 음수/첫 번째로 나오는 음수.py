def solution(num_list):
    answer = 0
    for i in range(len(num_list)):
        print(i)
        if int(num_list[i]) < 0:
            return i
    return -1
   