def solution(num_list):
    answer = 0
    astr = ''
    astr2 = ''
    for i in num_list:
        if i % 2 == 0:
            astr = astr + str(i)
            # print(astr)
        elif i % 2 == 1:
            astr2 = astr2 + str(i)
    answer = int(astr) + int(astr2)
    return answer