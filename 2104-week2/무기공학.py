'''
    https://www.acmicpc.net/problem/18430
    무기공학 - 백트래킹

    공학자 길동이는 외부의 침략으로부터 마을을 지킬 수 있는 부메랑 무기를 개발한다.
    부메랑을 만들기 위해 필요한 고급 나무 재료는 NxM 크기이며, 직사각형의 부위마다 그 강도가 조금씩 다르다.
    부메랑은 항상 3칸을 차지하는 'ㄱ' 모양으로 만들어야한다.
    이때, 부메랑의 중심이 되는 칸은 강도의 영향을 2배로 받는다. 
    그리고 나무 재료의 특정 위치는 아예 사용하지 않아도 괜찮다. 
    나무 재료의 형태와 각 칸의 강도가 주어졌을 때, 길동이가 만들 수 있는 부메랑들의 강도 합의 최댓값을 출력하시오.
'''
import sys
answer = 0

dirr = [[1,-1],[-1,-1],[1,1],[-1,1]] # 아래왼, 위왼, 아래오른, 위오른
N,M = 0,0
block = []

def solution(N,M,block):
    visited = [[0 for _ in range(M)] for _ in range(N)]
    backTracking(0,0,visited,0)
    return answer

def backTracking(x,y,visited,summ):
    global N,M,answer,block
    if y == M:
        y = 0
        x += 1
    if x == N:
        answer = max(answer, summ)
        return
    
    if not visited[x][y]:
        for dx,dy in dirr:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][y] and not visited[x][ny]:
                visited[x][y] = True
                visited[x][ny] = True
                visited[nx][y] = True
                nsum = summ + makeSum(x,y,nx,ny,block)
                backTracking(x,y+1,visited,nsum)
                visited[x][y] = False
                visited[x][ny] = False
                visited[nx][y] = False
    backTracking(x,y+1,visited,summ)
            
def makeSum(x,y,nx,ny,block):
    return 2*block[x][y] + block[nx][y] + block[x][ny]

if __name__=='__main__':
    N,M = map(int,sys.stdin.readline().rstrip().split())

    for i in range(0,N):
        input = list(map(int,sys.stdin.readline().rstrip().split()))
        block.append(input)

    solution(N,M,block)
    print(answer)