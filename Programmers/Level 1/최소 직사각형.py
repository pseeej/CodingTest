def solution(sizes):
    answer = 0
    
    newsizes = []
    reswidth = 0
    resheight = 0
    for size in sizes:
        width, height = size
        if width > height:
            reswidth = max(reswidth, width)
            resheight = max(resheight, height)
        else:
            reswidth = max(reswidth, height)
            resheight = max(resheight, width)
            
    answer = reswidth*resheight
            
    
    return answer
