'''
    N x M 크기의 직사각형, 각각의 칸은 육지 또는 바다이다.
    캐릭터는 동서남북 중 한 곳을 바라본다.
    맵의 각 칸은 (A,B)로 나타내며, 바다로된 공간에는 갈 수 없다.

    1. 현재 위치에서 현재 방향을 기준으로 왼쪽 방향(반시계) 부터 차례대로 갈 곳을 정한다.
    2. 캐릭터의 바로 왼쪽 방향에 가보지 않은 칸이 있으면, 캐릭터를 왼쪽 방향으로 회전한 다음 왼쪽으로 한 칸을 전진한다. 
    가보지 않은 칸이 없다면 캐릭터의 방향을 왼쪽으로 회전한 후, 1단계로 돌아간다.
    3. 만약 네 방향 모두 가본 칸이거나 바다로 되어 있는 칸인 경우, 바라보는 방향을 유지한 채로 한칸 뒤로 가고 1단계로 돌아간다.
    단, 이때 뒤쪽 방향이 바다인 칸이라 뒤로 돌아갈 수 없는 경우에는 움직임을 멈춘다.

    이때, 캐릭터가 방문한 칸의 수를 출력하시오
'''
import sys

# dirr - 0은 북, 1은 동, 2는 남, 3은 서
def movingTest(N,M,x,y,dirr,space):

    dx = [0,-1,0,1] #서,북,동,남 - 캐릭터의 시선에서 왼쪽 방향 배열
    dy = [-1,0,1,0]
    record = [[0 for i in range(M)] for j in range(N)]
    record[x][y] = 1
    answer = 1
    turns = 0

    while (True):
        # 방향 전환
        if ( dirr == 0 ):
            dirr = 3
        else:
            dirr -= 1

        # 현재 내 캐릭터의 왼쪽방향 살피기
        nx = x + dx[dirr]
        ny = y + dy[dirr]

        # 왼쪽방향이 갈 수 있고, 바다가 아니고, 간 적이 없을 때
        if ( nx >= 0 and nx < N and ny >= 0 and ny < M and space[nx][ny] != 1 and record[nx][ny] != 1):
            x,y = nx,ny
            turns = 0
            answer += 1
            record[x][y] = 1
            continue
        
        turns += 1
        # 갈 수 있는 곳이 없다.
        if ( turns == 4 ):
            nx = x + dx[dirr]
            ny = y + dy[dirr]
            if ( nx >= 0 and nx < N and ny >= 0 and ny < M and space[nx][ny] != 1):
                x,y = nx, ny
                turns = 0
            else:
                break
    return answer

if __name__ == '__main__':
    space = []
    N,M = map(int,sys.stdin.readline().rstrip().split(" "))
    x,y,dirr = map(int,sys.stdin.readline().rstrip().split(" "))
    for i in range(0,N):
        space.append(list(map(int,sys.stdin.readline().rstrip().split())))
    print(movingTest(N,M,x,y,dirr,space))
