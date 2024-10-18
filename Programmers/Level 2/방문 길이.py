def solution(dirs):
    answer = 0
    
    d = {'U':(1, 0), 'D':(-1, 0), 'R':(0, 1), 'L':(0, -1)}
    visited = set()
    
    y, x = 0, 0
    for way in dirs:
        dy, dx = d[way]
        if -5 <= y+dy <= 5 and -5 <= x+dx <= 5:
            visited.add(((y, x), (y+dy, x+dx)))
            visited.add(((y+dy, x+dx), (y, x)))
            y, x = y+dy, x+dx
    
    result = set()
    for point in visited:
        left, right = point
        if not((left, right) in result or (right, left) in result):
            result.add((left, right))
    
    return len(result)
