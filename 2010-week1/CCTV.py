# 백준 15683번 문제 : 감시
'''
스타트링크의 사무실은 1×1크기의 정사각형으로 나누어져 있는 N×M 크기의 직사각형으로 나타낼 수 있다
 사무실에는 총 K개의 CCTV가 설치되어져 있는데, CCTV는 5가지 종류가 있다. 각 CCTV가 감시할 수 있는 방법은 다음과 같다.
 
 1번 CCTV는 한 쪽 방향만 감시할 수 있다. 2번과 3번은 두 방향을 감시할 수 있는데, 
 2번은 감시하는 방향이 서로 반대방향이어야 하고,
 3번은 직각 방향이어야 한다.
 4번은 세 방향, 5번은 네 방향을 감시할 수 있다.
 지도에서 0은 빈 칸, 6은 벽, 1~5는 CCTV의 번호이다. 

CCTV는 감시할 수 있는 방향에 있는 칸 전체를 감시할 수 있다.
사무실에는 벽이 있는데, CCTV는 벽을 통과할 수 없다. CCTV가 감시할 수 없는 영역은 사각지대라고 한다.
CCTV는 회전시킬 수 있는데, 회전은 항상 90도 방향으로 해야 하며, 감시하려고 하는 방향이 가로 또는 세로 방향이어야 한다.
CCTV는 CCTV를 통과할 수 있다

사무실의 크기와 상태, 그리고 CCTV의 정보가 주어졌을 때, CCTV의 방향을 적절히 정해서,
사각 지대의 최소 크기를 구하는 프로그램을 작성하시오.
'''

# 입력
'''
첫째 줄에 사무실의 세로 크기 N과 가로 크기 M이 주어진다. (1 ≤ N, M ≤ 8)
둘째 줄부터 N개의 줄에는 사무실 각 칸의 정보가 주어진다. 0은 빈 칸, 6은 벽, 1~5는 CCTV를 나타내고, 문제에서 설명한 CCTV의 종류이다. 
CCTV의 최대 개수는 8개를 넘지 않는다.
'''

# 출력
'''
첫째 줄에 사각 지대의 최소 크기를 출력한다.
'''
import sys
import copy

res = 100 # 사각지대 최소값
dirr = [[1,0],[-1,0],[0,1],[0,-1]] #북, 남, 동, 서
space = [] # 전체 공간
cctv = [] # cctv

# cctv 체크
def dfs(cnt):
    global res

    # 최소값 갱신
    new = 0
    if ( cnt == len(cctv)):
        for i in range(N):
            for j in range(M):
                if space[i][j] == 0:
                    new += 1
        res = min(res,new)
        return res

    # preview copy
    prev = copy.deepcopy(cctv)

    # cctv 좌표
    now_x = cctv[cnt][0]
    now_y = cctv[cnt][1]
    now_cam = cctv[cnt][2]

    # cctv 탐색
    if ( now_cam == 1 ): # 북,남,동,서
        for i in range(4):
            turn(i,now_x,now_y)
            dfs(cnt+1)
            cctv = prev
    elif ( now_cam == 2 ): # 북남, 동서
        for i in range(2):
            turn(2*i,now_x,now_y)
            turn(2*i+1,now_x,now_y)
            dfs(cnt+1)
            cctv = prev
    elif ( now_cam == 3 ): # 북동, 동남, 남서, 서북 03 13 02 12   
        for i in range(4):  #0 1 2 3
            turn(i%2,now_x,now_y)
            turn(,now_x,now_y)
    elif ( now_cam == 4 ): # 서북동, 북동남, 동남서,남서북
        for i in range(4):

    elif ( now_cam == 5 ): # 모든 방향임으로 cctv 배열 수정 필요 없음
        for i in range(4):
            turn(i,now_x,now_y)
        dfs(cnt+1)

def turn(d,x,y):
    # 북 마킹
    if ( d == 0 ):
        for i in reversed(range(x-1)):
            if ( cctv[i][y] == 6) : break
            cctv[i][y] = -1
        return
    # 남 마킹
    elif ( d == 1 ):
        for i in range(x+1):
            if ( cctv[i][y] == 6) : break
            cctv[i][y] = -1
        return
    # 동 마킹
    elif ( d == 2 ):
        for i in range(y+1)):
            if ( cctv[x][i] == 6) : break
            cctv[x][i] = -1
        return
    # 서 마킹
    elif ( d == 3 ):
        for i in reversed(range(y-1)):
            if ( cctv[x][i] == 6) : break
            cctv[x][i] = -1
        return

if __name__ == '__main__':
    global space, cctv
    var = list(map(int,sys.stdin.readline().rstrip().split(" ")))
    N = var[0] # R : 가로 행 개수
    M = var[1] # L : 세로 열 개수
    for i in range(0,N):
        space.append(list(map(int,sys.stdin.readline().rstrip().split())))
        for j in range(0,M):
            if (space[i][j] != 0 or space[i][j] != 6): # cctv라면
                cctv.append([i,j,space[i][j]])

    print(dfs(0))

'''
6 6
0 0 0 0 0 0
0 2 0 0 0 0
0 0 0 0 6 0
0 6 0 0 2 0
0 0 0 0 0 0
0 0 0 0 0 5
'''