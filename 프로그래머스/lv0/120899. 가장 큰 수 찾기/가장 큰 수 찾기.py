def solution(array):
    number = max(array)
    return [number,array.index(number)]
#     answer = []
#     array2 = sorted(array)
#     answer.append(array2[-1])
#     print(array2)
#     for i in range(len(array)):
#         if array[i] == array2[-1]:
#             answer.append(i)
    
#     return answer
    