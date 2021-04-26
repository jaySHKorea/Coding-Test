'''
    https://www.acmicpc.net/problem/3109
    원웅이는 지출을 줄이고자 가스비를 줄이려고 한다. 근처 빵집의 가스관에 몰래 파이프를 설치해 훔쳐서 사용하기로 했다.
    빵집이 있는 곳은 R*C 격자로 표현된다. 첫째 열은 근처 빵집의 가스관, 마지막 열은 원웅이의 빵집이다.
    
    원웅이는 가스관과 빵집을 연결하는 파이프를 설치하려고 한다.
    빵집과 가스관 사이에는 건물이 있을 수도 있다. 건물이 있을 경우 파이프를 놓을 수 없다.
    가스관과 빵집을 연결하는 모든 파이프라인은 첫쨰 열에서 시작하며, 마지막 열에서 끝난다.
    각 칸은 오른쪽, 오른쪽 위 대각선, 오른쪽 아래 대각선으로 연결할 수 있고, 각 칸의 중심끼리 연결하는 것이다.
    원웅이는 가스를 되도록 많이 훔치려고 한다. 따라서, 가스관과 빵집을 연결하는 파이프라인을 여러 개 설치할 것이다.
    이 경로는 겹칠 수 없고 서로 접할 수도 없다. 각 칸의 파이프는 하나이다.
    원웅이의 빵집 모습이 주어졌을 떄, 원웅이가 설치할 수 있는 가스관과 빵집을 연결하는 파이프라인의 최대 개수를 구하시오.
'''
# dfs+Greedy
import sys
answer = 0
dirr = [ -1,0,1]

def solution(R,C,pipe):
    global answer
    for i in range(1,R+1):
        dfs(i,1,R,C)
    return answer

def dfs(x,y,R,C):
    global answer
    if y == C:
        answer += 1
        return True

    for dir in dirr:
        nx = x+dir
        ny = y+1
        if pipe[nx][ny] != -1 and ny <= C:
            result = dfs(nx,ny,R,C)
            pipe[nx][ny] = -1 # Greedy : 가능/불가능 상관없이 갔다면 무조건 visited
            if result:
                return True
    return False

if __name__=='__main__':
    R,C = map(int,sys.stdin.readline().rstrip().split())
    pipe = [[-1 for _ in range(C+2)] for _ in range(R+2)]

    for i in range(1,R+1):
        input = list(sys.stdin.readline().rstrip())
        for j in range(1,C+1):
            if j == 1 or input[j-1] == '.':
                pipe[i][j] = 1
            elif input[j-1] == 'x':
                pipe[i][j] = -1
            else:
                pipe[i][j] = 0
    print(solution(R,C,pipe))