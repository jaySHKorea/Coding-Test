'''
    1h, 삭제기능 수정해야함

    구현 12 - 기둥과 보 설치
    2020 카카오 신입 공채

    기둥과 보를 이용하여 벽면구조물을 자동으로 세우는 로봇을 개발할 계획이다.
    그에 앞서 로봇의 동작을 시뮬레이션 할 수 있는 프로그램을 만들고 있습니다.

    2차원 가상 벽면에 기둥과 보를 이용한 구조물을 설치할 수 있는데, 
    기둥과 보는 길이가 1인 선분으로 표현되며 다음과 같은 규칙을 가지고 있다.

    1. 기둥은 바닥 위에 있거나 보의 한쪽 끝 부분 위에 있거나, 또는 다른 기둥위에 있어야 합니다.
    2. 보는 한쪽 끝 부분이 기둥 위에 있거나, 또는 양쪽 끝부분이 다른 보와 동시에 연결되어 있어야 합니다.

    2차원 벽면은 N x N 크기 정사각 격자 형태이며, 맨 처음 벽면은 비어 있다.  
'''

from collections import deque

'''
    기둥과 보는 각각 3가지의 설치가능조건이 있다.
    설치/삭제는 조건이 같다.

    어떤 요소를 설치했을 때(queue 삽입), 설치된 모든 요소 중 조건에 어긋나는게 생긴다면 설치불가(queue 제거)
    어떤 요소를 삭제했을 때(queue 제거), 설치된 모든 요소 중 조건에 어긋나는게 생긴다면 삭제불가(queue 삽입)
'''
def check(result):
    col, beam = 0, 1
    for x, y, a in result:
        if a == col: # 기둥일 때
            if y != 0 and (x, y-1, col) not in result and (x-1, y, beam) not in result and (x, y, beam) not in result:
                return False
        else: # 보일 때
            if (x, y-1, col) not in result and (x+1, y-1, col) not in result and not ((x-1, y, beam) in result and (x+1, y, beam) in result):
                return False
    return True

def solution(n, build_frame):
    result = deque()
    for x, y, a, build in build_frame:
        item = (x, y, a)
        if build: # 추가일 때
            result.append(item)
            if check(result) == False:
                result.remove(item)
        elif item in result: # 삭제할 때
            result.remove(item)
            if check(result) == False:
                result.append(item)

    answer = list(result)
    return sorted(answer, key = lambda x : (x[0], x[1], x[2]))

print(solution(5,[[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]))
print(solution(5, [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]))