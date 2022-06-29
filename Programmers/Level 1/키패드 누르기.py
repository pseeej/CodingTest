# 값 주어지면 해당 값의 위치를 tuple 형태로 반환
def getLocation(num):
    if num == '#':
        return (3, 2)
    if num == '*':
        return (3, 0)
    if num == 0:
        return (3, 1)
    
    return ((num-1)//3, (num-1)%3)

# 현재 위치 숫자값으로 확인 위해 location으로 표현되어있던 것 값으로 변경
# *은 10, 0은 11, 1은 12로 나타남
def Loc2Num(loc):
    return loc[0]*3 + loc[1] + 1

def solution(numbers, hand):
    answer = ''
    
    # 왼손이 입력 가능한 값, 오른손이 입력 가능한 값을 저장한 리스트 따로 선언
    leftnums=[1, 4, 7, '*']
    rightnums = [3, 6, 9, '#']

    # 현재 위치로 초기화. 왼손은 *, 오른손은 #
    leftnow = getLocation('*')
    rightnow = getLocation('#')
    
    # 입력받은 numbers에서 숫자 하나씩 돌면서 진행
    for num in numbers:
        # 왼손으로만 입력 가능할 경우
        # 왼손의 위치 갱신 후 최종적으로 return할 문자열에 L 추가
        if num in leftnums:
            leftnow = getLocation(num)
            answer+='L'
        # 오른손으로만 입력 가능한 경우
        # 오른손의 위치 갱신 후 최종적으로 return할 문자열에 R 추가
        elif num in rightnums:
            rightnow = getLocation(num)
            answer += 'R'
        # 왼손과 오른손 모두 입력 가능한 키인 경우
        else:
            # num의 위치 받아서
            numLoc = getLocation(num)
            
            # 왼손, 오른손의 위치와 거리 계산
            left_num = abs(numLoc[0]-leftnow[0]) + abs(numLoc[1]-leftnow[1])
            right_num = abs(numLoc[0]-rightnow[0]) + abs(numLoc[1]-rightnow[1])
            
            # 왼손에서의 위치, 오른손에서 위치를 비교해서
            # 왼손이 더 가까이 있으면 왼손 선택,
            # 오른손이 더 가까이 있으면 오른손 선택
            if left_num < right_num:
                leftnow = getLocation(num)
                answer += 'L'
            elif left_num > right_num:
                rightnow = getLocation(num)
                answer += 'R'
            # 거리가 같을 경우 왼손잡이인지 오른손잡이인지 판단 후 이동
            else:
                if hand=="left":
                    leftnow = getLocation(num)
                    answer += 'L'
                else:
                    rightnow = getLocation(num)
                    answer += 'R'               

    return answer
