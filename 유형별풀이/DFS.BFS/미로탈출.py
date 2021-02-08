'''
    동빈이는 N X M 크기의 직사각형 형태의 미로에 갇혀 있다. 미로에는 여러 마리의 괴물이 있다.
    동빈의 위치는 (1,1)이고 미로의 출구는 (N,M)의 위치에 존재한다.
    한번에 한칸씩 이동할 수 있고, 괴물이 있는 부분은 0, 괴물이 없는 부분은 1이다.
    이때 동빈이가 탈출하기 위해 움직여야 하는 최소 칸의 개수를 구하시오
'''
import sys
from collections import deque

def outMaze(N,M,maze):
    move = [[-1,0],[1,0],[0,-1],[0,1]] #상하좌우-1,2,3,4
    queue = deque()
    queue.append((0,0,-1))

    while queue :
        x,y,dirr = queue.popleft() # x좌표, y좌표, 자기가 온 방향

        # 동서남북 탐색
        for i in range(4):
            if ( dirr == i):continue
            nx = x+move[i][0]
            ny = y+move[i][1]
            # 값을 벗어난 경우
            if ( nx < 0 or nx >= N or ny < 0 or ny >= M):
                continue
            # 괴물일 때
            if ( maze[nx][ny] == 0):
                continue
            # 괴물이 없고 한번도 방문하지 않은 곳
            if ( maze[nx][ny] == 1):
                maze[nx][ny] = maze[x][y]+1
                if ( i >= 2 ):
                    queue.append((nx,ny,(i+1)%2+2))
                else:
                    queue.append((nx,ny,(i+1)%2))
    return maze[N-1][M-1]

if __name__ == '__main__':
    maze = []
    N,M = map(int,input().split())
    for i in range(N):
        maze.append(list(map(int,input())))
    print(outMaze(N,M,maze))