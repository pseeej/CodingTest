def solution(progresses, speeds):
    answer = []
    
    # 먼저 들어온 게 top이 되는 stack 형태로 생각
    prog_st = progresses
    speed_st = speeds
    
    top = 0
    # 스택이 비면 종료
    while len(prog_st) > 0:
        # 하루가 지나면서 진도 갱신
        for i in range(len(prog_st)):
            prog_st[i] += speed_st[i]
        
        # 하루에 배포되는 서비스 개수 세기 위한 변수
        cnt = 0
        # 만약 배포될 준비가 완료된 서비스가 top에 있을 경우
        while prog_st[top] >= 100:
            # 종료 조건. 스택에 값이 하나밖에 남지 않았을 경우
            if len(prog_st) == 1:
                prog_st = []
                cnt += 1
                break
            # 100% 이상이 된 작업은 배포가 완료되었으므로 pop 진행
            prog_st = prog_st[1:]
            speed_st = speed_st[1:]
            # 배포 완료한 작업 개수 갱신
            cnt += 1
        
        # 하나 이상의 작업이 배포되었을 경우 answer 배열에 추가
        if cnt != 0:
            answer.append(cnt)
            
    return answer
