def solution(babbling):
    answer = 0
    for i in babbling:
        if "aya" in i:
            i = i.replace("aya",".")
        if "ye" in i:
            i = i.replace("ye",".")
        if "woo" in i:
            i = i.replace("woo",".")
        if "ma" in i:
            i = i.replace("ma",".")
        print(i)
        i = i.replace(".","")
        # print(i)
        if not i:
            answer += 1
            
    return answer

