def solution(s):
    answer = 0
    numbers = {
        'zero': "0",
        'one': "1",
        'two': "2",
        'three': "3",
        'four': "4",
        'five': "5",
        'six': "6",
        'seven': "7",
        'eight': "8",
        'nine': "9"
}
    for i in numbers:
        # print(i)
        # if i not in s:
            # continue
        # if i in s:
        # print(i)
        s = s.replace(i, numbers[i])
    # print(s)
    return int(s)