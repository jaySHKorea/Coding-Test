'''
    https://www.acmicpc.net/problem/10836
 
    크기가 MxM인 격자 형태의 벌집이 있다. 이 벌집의 각 칸에는 여왕벌이 될 애벌레들이 한 마리씩 자라고 있다.
    격자칸의 좌표계를 다음과 같이 설정한다. 제일 왼쪽 위 칸은 (0,0)

    애벌레들은 매일 에너지를 모아서 정오(낮 12시)에 한번 자란다. 첫날 아침 모든 애벌레들의 크기는 1이고, N일 동안 반복한다.

    각 애벌레가 자라서 크기가 커지는 정도는 하루에 0,1,2 세가지 중 하나이다.
    제일 왼쪽 열의 아래부터 위쪽으로, 도착하면 오른쪽으로 가면서 읽는다.

    나머지 애벌레들은 자신의 왼쪽, 왼쪽 위, 위쪽의 애벌레들이 다 자란 다음, 그날 가장 많이 자란 애벌레가 자란 만큼 자기도 자란다.
'''
import sys

def solution(N,M,grow):
    week_grow = [0 for _ in range(2*M-1)]
    for i in range(N):
        for j in range(grow[i][0],grow[i][0]+grow[i][1]):
            week_grow[j] += 1
        for j in range(grow[i][0]+grow[i][1],2*M-1):
            week_grow[j] += 2

    new_map = [[1 for _ in range(M)] for _ in range(M)]

    growing_line(M,week_grow,new_map)
    growing(M,new_map)
    
    for i in range(M):
        for j in range(M):
            print(new_map[i][j],end=' ')
        print()

def growing_line(M,week_grow,new_map):
    here = 0
    
    for i in range(M-1,-1,-1):
        new_map[i][0] += week_grow[here]
        here += 1

    for i in range(1,M):
        new_map[0][i] += week_grow[here]
        here += 1

def growing(M,new_map):
    for i in range(1,M):
        for j in range(1,M):
            new_map[i][j] += new_map[0][j]-1 # 중요! 왼위 테두리의 자라는 정도는 안 감소하므로, 왼/왼쪽대각선/위 중에서 가장 큰 자람은 위쪽이므로, 젤 위칸 위쪽만 살피면 됨
    
if __name__=='__main__':
    M,N = map(int,sys.stdin.readline().rstrip().split())
    grow = []

    for i in range(0,N):
        input = list(map(int,sys.stdin.readline().rstrip().split()))
        grow.append(input)

    solution(N,M,grow)