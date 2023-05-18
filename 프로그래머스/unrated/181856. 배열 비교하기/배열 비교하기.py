def solution(arr1, arr2):
    a = 0
    b = 0
    if len(arr1) < len(arr2):
        return -1
    if len(arr1) > len(arr2):
        return 1
    if len(arr1) == len(arr2):
        for i in range(len(arr1)):
            a += arr1[i]
            b += arr2[i]
    if a > b:
        return 1
    if a < b:
        return -1
    if a == b:
        return 0