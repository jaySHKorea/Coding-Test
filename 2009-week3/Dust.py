# 백준 17144번 미세먼지 안녕!
'''
미세먼지를 제거하기 위해 구사과는 공기청정기를 설치하려고 한다.
공기청정기의 성능을 테스트하기 위해 구사과는 집을 크기가 R×C인 격자판으로 나타냈고, 1×1 크기의 칸으로 나눴다.
구사과는 뛰어난 코딩 실력을 이용해 각 칸 (r, c)에 있는 미세먼지의 양을 실시간으로 모니터링하는 시스템을 개발했다.
(r, c)는 r행 c열을 의미한다.

공기청정기는 항상 1번 열에 설치되어 있고, 크기는 두 행을 차지한다.
공기청정기가 설치되어 있지 않은 칸에는 미세먼지가 있고, (r, c)에 있는 미세먼지의 양은 Ar,c이다.

1초 동안 아래 적힌 일이 순서대로 일어난다.

미세먼지가 확산된다. 확산은 미세먼지가 있는 모든 칸에서 !동시에! 일어난다.
(r, c)에 있는 미세먼지는 인접한 네 방향으로 확산된다.
인접한 방향에 공기청정기가 있거나, 칸이 없으면 그 방향으로는 확산이 일어나지 않는다.
확산되는 양은 Ar,c/5이고 소수점은 버린다.
(r, c)에 남은 미세먼지의 양은 Ar,c - (Ar,c/5)×(확산된 방향의 개수) 이다.
공기청정기가 작동한다.
공기청정기에서는 바람이 나온다.
위쪽 공기청정기의 바람은 반시계방향으로 순환하고, 아래쪽 공기청정기의 바람은 시계방향으로 순환한다.
바람이 불면 미세먼지가 바람의 방향대로 모두 한 칸씩 이동한다.
공기청정기에서 부는 바람은 미세먼지가 없는 바람이고, 공기청정기로 들어간 미세먼지는 모두 정화된다.
'''

# 입력
'''
첫째 줄에 R, C, T (6 ≤ R, C ≤ 50, 1 ≤ T ≤ 1,000) 가 주어진다.

둘째 줄부터 R개의 줄에 Ar,c (-1 ≤ Ar,c ≤ 1,000)가 주어진다.
공기청정기가 설치된 곳은 Ar,c가 -1이고, 나머지 값은 미세먼지의 양이다.
-1은 2번 위아래로 붙어져 있고, 가장 윗 행, 아랫 행과 두 칸이상 떨어져 있다.
'''

# 출력
'''첫째 줄에 T초가 지난 후 구사과 방에 남아있는 미세먼지의 양을 출력한다.'''

import sys
import copy
from collections import deque

machine = -1
m_loc = [] # 공기청정기 위치
dx = [ 0, 0, 1, -1 ] # 위 아래 오 왼
dy = [ -1, 1, 0, 0 ]
ba = [ 2, 0, 3, 1 ] # 반시계
fo = [ 2, 1, 3, 0 ] # 시계

def solution(R,C,T,A):
    answer = 0

    while ( T != 0 ):
        # 1초 지남
        T -= 1
        spread(R,C,T,A)
        A_copy = copy.deepcopy(A)
        circulate(m_loc[0], ba, A, A_copy)
        circulate(m_loc[1], fo, A, A_copy)
    
    answer = sum(sum(x) for x in A)
    return answer

def spread(R,C,T,A):
    global m_loc
    q = deque()

    for i in range(R):
        for j in range(C):
            if (A[i][j] >= 5): # 5가 넘어야 확산되는 미세먼지가 있음
                q.append([i, j, A[i][j]])
            elif ( A[i][j] == -1): # 기계라면 index append
                m_loc.append(i)

    while (len(q) != 0):
        dust = q.popleft()
        s_dust = int(dust[2] / 5)
        cnt = 0
 
        for k in range(4):  # 위 아래 오 왼
            nx = dust[1] + dx[k] 
            ny = dust[0] + dy[k] 
 
            if ( nx >= 0 and nx < C and ny >= 0 and ny < R): # 인덱스 벗어나지 않았을 때
                if (A[ny][nx] != machine): # 기계가 아니라면
                    cnt += 1 # 확산 개수
                    A[ny][nx] += s_dust # 확산
                
        A[dust[0]][dust[1]] -= s_dust*cnt # 빼주기

def circulate(mach,dirr,A,A_copy): 
    # ba(반시계) : 오->위->왼->아래
    # fo (시계) : 오->아래->왼->위
    x = mach
    y = 0
    A_copy[x][y] = 0
    for k in range(4): #
        while True:
            nx = y + dx[dirr[k]]
            ny = x + dy[dirr[k]]
            if (not ( ny >= 0 and ny < R and nx >= 0 and nx < C)): # 인덱스 끝을 만났거나
                break
            if ( ny == mach and nx == 0 ): # 다시 제자리로 돌아왔을 때
                break
            A[ny][nx] = A_copy[x][y]
            y = nx
            x = ny

if __name__ == '__main__':
    A = [] # 입력배열
    var = list(map(int,sys.stdin.readline().rstrip().split(" ")))
    R = var[0] # R : 가로 행 개수
    C = var[1] # L : 세로 열 개수
    T = var[2] # T : ~초 이후
    for i in range(0,R):
        A.append(list(map(int,sys.stdin.readline().rstrip().split()))) # 경사로 배열 입력 받기 list(map(int, list_a))
    print(solution(R,C,T,A)+2)