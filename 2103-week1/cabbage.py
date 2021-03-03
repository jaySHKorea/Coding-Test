'''
    BOJ 1012 유기농 배추 - dfs

    어떤 배추에 배추흰지렁이가 한 마리라도 살고 있으면, 이 지렁이는 인접한 다른 배추로 이동할 수 있고, 배추들은 보호 받을 수 있다.

    땅은 고르지 못하기에 배추를 군데군데 심어놓았다. 

    입력의 첫줄은 테스트 케이스 개수 T
        둘쨋줄에 가로길이 M, 세로길이 N, 배추개수 K, 그 다음 K줄에 배추의 위치 X,Y가 주어진다.
'''
import sys

move = [[1,0],[-1,0],[0,1],[0,-1]]

def solution(array,M,N):
    answer = 0
    for i in range(N):
        for j in range(M):
            if array[i][j] == 1:
                dfs(i,j,array)
                answer += 1
    return answer

def dfs(i,j,array):
    sys.setrecursionlimit(10 ** 5) # 재귀 리밋
    array[i][j] = 0
    for m in move:
        nx = i+m[0]
        ny = j+m[1]
        if (nx >= 0 and nx < N and ny >= 0 and ny < M and array[nx][ny] == 1):
            dfs(nx,ny,array)
    
if __name__ == '__main__':
    ans = []
    cnt = int(input())
    for i in range(cnt):
        var = list(map(int,sys.stdin.readline().rstrip().split(" ")))
        M = var[0] # L : 세로 열 개수
        N = var[1] # R : 가로 행 개수 
        K = var[2] # 배추개수
        array = [[0 for _ in range(M)] for _ in range(N)]
        for j in range(K):
            where = list(map(int,sys.stdin.readline().rstrip().split()))
            array[where[1]][where[0]] = 1
        ans.append(solution(array,M,N))
    
    for a in ans:
        print(a)