def solution(s):
    stack = []
    for char in s:
        if char == "(":
            stack.append(char)
        elif char == ")":
            if len(stack) == 0:  # 스택이 비어있으면 올바르지 않은 괄호
                return False
            stack.pop()
    
    if len(stack) == 0:  # 모든 괄호가 올바르게 짝지어져 있으면 스택이 비어있어야 함
        return True
    else:
        return False