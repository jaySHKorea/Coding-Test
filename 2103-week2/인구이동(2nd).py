'''
    dfs/bfs 07 백준 16234 40m dfs 버전

    N x N 크기의 땅이 있고 1 x 1로 나누어져 있다. 각땅에는 나라가 하나씩 존재하며, r행 c열의 나라에는 A[r][c]명이 살고 있다.
    인전합 나라 사이에는 국경선이 존재한다. 국경선은 정사각형 형태이다

    인구이동이 다음과 같이 일어나며, 더이상 아래 방법에 의해 이동이 없을 때까지 지속됩니다.

    1. 국경선을 공유하는 두 나라의 인구 차이가 L명 이상 R명 이하라면 두 나라가 공유하는 국경선을 오늘 하루동안 엽니다.
    2. 위의 조건에 의해 열어야하는 국경선이 모두 열렸다면 인구이동을 시작
    3. 국경선이 열려있어 인접한 칸만을 이용해 이동할 수 있으면 그 나라를 오늘 하루 동안 연합이라고 한다.
    4. 연합을 이루고 있는 각 칸의 인구수는 연합의 인구수/연합을 이루고 있는 칸의 개수가 됩니다. 소수점음 버립니다.
    5. 연합을 해체하고 모든 국경선을 닫습니다.

    각 나라의 인구수가 주어졌을 때, 인구이동이 몇번 발생하는지 구하시오
'''
import sys

dirr = [[-1,0],[1,0],[0,-1],[0,1]]

def solution(N,L,R,country):
    answer = 0
    
    while True:
        uni = []
        flag = False
        visited = [[0 for _ in range(N)] for _ in range(N)]
        
        # 연합생성
        for i in range(N):
            for j in range(N):
                if visited[i][j] == 0:
                    temp = []
                    temp.append((country[i][j],i,j))
                    uni.append(dfs(i,j,visited,temp))

        # 인구이동
        for u in uni:
            if len(u) > 1:
                move(u)
                flag = True
        # 인구이동이 일어나지 않는다면
        if flag == False:
            return answer
        answer += 1

# 연합 만들기
def dfs(i,j,visited,union):
    visited[i][j] = 1
    for d in dirr:
        x = i+d[0]
        y = j+d[1]
        if 0 <= x < N and 0 <= y < N and visited[x][y] == 0 and L <= abs(country[i][j]-country[x][y]) <= R :
            union.append((country[x][y],x,y))
            dfs(x,y,visited,union)
    return union

# 인구 이동
def move(u):
    sum = 0
    for i in range(len(u)):
        sum += u[i][0]
    
    sep = int(sum/len(u))

    for c,i,j in u:
        country[i][j] = sep

if __name__ == '__main__':
    N,L,R = map(int,sys.stdin.readline().rstrip().split(" "))

    country = []
    for i in range(N):
        var = list(map(int,sys.stdin.readline().rstrip().split(" ")))
        country.append(var)
    
    print(solution(N,L,R,country))