def solution(spell, dic):
    arr = []
    
    
    
    for i in dic:
        if sorted(spell) == sorted(i):
            print()
            return 1
            
    return 2