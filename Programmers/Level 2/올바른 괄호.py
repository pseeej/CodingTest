def solution(sent):
    answer = True
    
    stack = []
    for s in sent:
        if s == "(":
            stack.append(s)
        else:
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                return False
            
    if len(stack):
        return False

    return True
