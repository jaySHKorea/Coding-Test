'''
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

def solution(n, build_frame):
    answer = deque()
    col = [[0 for _ in range(n+1)] for _ in range(n+1)] # 기둥 배열
    beam = [[0 for _ in range(n+1)] for _ in range(n+1)] # 보 배열

    for build in build_frame:
        x,y = build[0],build[1]
        sep = build[2] # 0은 기둥 1은 보
        br = build[3] # 0은 삭제 1은 설치

        # 기둥일 때
        if sep == 0:
            # 설치 일때
            if br == 1:
                # 바닥에 놓을 때
                if y == 0:
                    answer.append([x,y,0])
                    col[x][y] = 1
                else:
                    if beam[x-1][y] == 1 or beam[x][y] == 1 or col[x][y-1] == 1:
                        answer.append([x,y,0])
                        col[x][y] = 1
            # 삭제 일때
            else:
                flag = False
                if beam[x][y+1] == 0 and beam[x-1][y+1] == 0:
                    flag = True
                else:
                    if beam[x][y+1] == 1 and col[x+1][y] == 1:
                        flag = True
                    else:
                        flag = False
                    if beam[x-1][y+1] == 1 and col[x-1][y] == 1:
                        flag = True
                    else:
                        flag = False
                if flag == True:
                    answer.remove([x,y,0])
                    col[x][y] = 0
        # 보일 때
        else:
            if br == 1:
                if col[x][y-1] == 1:
                    answer.append([x,y,1])
                    beam[x][y] = 1
                elif col[x+1][y-1] == 1:
                    answer.append([x,y,1])
                    beam[x][y] = 1
                elif beam[x-1][y] == 1 and beam[x+1][y] == 1:
                    answer.append([x,y,1])
                    beam[x][y] = 1
            # 삭제
            else:
                flag = False
                if beam[x-1][y] == 0 and beam[x+1][y] == 0:
                    flag = True
                else:
                    if beam[x-1][y] == 1 and (col[x][y-1] == 1 or col[x-1][y-1] == 1):
                        flag = True
                    else:
                        flag = False
                    if beam[x+1][y] == 1 and (col[x+1][y-1] == 1 and col[x+2][y-1] == 1):
                        flag = True
                    else:
                        flag = False
                if flag == True:
                    answer.remove([x,y,1])
                    beam[x][y] = 0
    
    answer = list(answer)
    answer = sorted(answer,key = lambda x : (x[0], x[1], x[2]))

    return answer

print(solution(5,[[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]))
print(solution(5, [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]))