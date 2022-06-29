def solution(s):
    answer = 0
    
    # 비교할 기준 길이. 제일 초기에 주어진 문자열의 길이로 설정.
    prevLen = len(s)
    
    # 잘리는 문자열이 최소 두 개 이상이어야 하기 때문에
    # 잘리는 길이를 len(s)//2까지로 제한. python range함수 특성 상 +1 해줌  
    for length in range(1, len(s)//2+1):
        # 현재 길이에서 나온 문자열 저장 위한 변수
        nowTxt = ""
        # 비교 대상이 되는 문자열 저장.
        prevWord = s[:length]
        # 다음 문자열의 시작 위치는 length부터.
        newIdx = length
        # 겹치는 개수 세어주기 위한 변수.
        # 일단 비교 대상의 단어도 하나로 포함되기 때문에 0이 아니라 1부터 시작
        cnt = 1
        
        # 새로 생성할 수 있는 length 길이의 문자열이 없을 때까지.
        while newIdx + length <= len(s):
            # 다음 문자열은 이전 문자열이 끝난 그 다음 위치에서부터
            # length의 길이를 가지게 됨. slicing 이용
            newWord = s[newIdx : newIdx+length]
            # 만약 비교 대상의 문자열과 현재의 문자열이 같을 경우
            # cnt변수 갱신
            if newWord == prevWord:
                cnt += 1
            # 다를 경우
            else:
                # 이전에 겹친 경우가 있을 때에는
                if cnt != 1:
                    # nowTxt에 cnt도 함께 집어넣어줌
                    nowTxt += str(cnt)+prevWord
                    # 비교 대상이 바뀌게 되므로 cnt값 초기화
                    cnt = 1
                # 이전에 겹친 경우가 없을 때
                else:
                    # 그냥 이전의 문자열을 넣어줌
                    nowTxt += prevWord
                # 비교 대상 갱신. 현재의 문자열로.
                prevWord = newWord
                
            # 시작 위치 변경.
            # 갱신된 비교 대상 문자열이 종료되는 위치부터 시작
            newIdx += length
        
        # 이전에 진행되던 내용이 처리되지 않고 종료되었을 때를 위한 부분
        if cnt != 1:
            nowTxt += str(cnt)+prevWord
        else:
            nowTxt += prevWord
            
        # 문자열로 만들어지지 못한 나머지 문자들을 붙여줌
        nowTxt += s[newIdx:]
        
        # 만약 새로 만든 문자열의 길이가 더 짧을 경우 길이 갱신
        if len(nowTxt) < prevLen:
            prevLen = len(nowTxt)
    
    answer = prevLen
    
    return answer
