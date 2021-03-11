'''
    dfs/bfs 03 30m 백준 18405

    N x N 크기의 시험관이 있습니다. 시험관은 1 x 1 크기의 칸으로 나누어지며, 특정  위치에는 바이러스가 존재할 수 있다.
    바이러스의 종류는 1~K번까지 K가지가 있으며, 모든 바이러스는 이 중 하나이다.

    시험관에 존재하는 모든 바이러스는 1초마다 상하좌우로 증식하는데, 매초 번호가 낮은 종류의 바이러스부터 먼저 증식합니다.
    또한 증식 과정에서 특정한 칸에 이미 어떠한 바이러스가 있다면, 그곳에는 다른 바이러스가 들어갈 수 없습니다.

    S초가 지난 후에 (X,Y)에 존재하는 바이러스의 종류를 출력하는 프로그램을 작성하세요.
'''

import sys
from collections import deque
import heapq
from copy import deepcopy

dirr = [[-1,0],[1,0],[0,-1],[0,1]]
heap = []

def solution(N,K,test,S,X,Y):
    global heap

    time = 0
    for i in range(N):
        for j in range(N):
            if test[i][j] != 0:
                heapq.heappush(heap,(test[i][j],i,j)) # K가 낮은대로 정렬되도록 : heap
    
    while time < S:
        time += 1
        how = deepcopy(heap)
        heap = []
        for i in range(len(how)):
            k,a,b = heapq.heappop(how)
            spread(a,b,test,k)

    return test[X-1][Y-1]

# 전염
def spread(i,j,test,K):
    for d in dirr:
        x = i+d[0]
        y = j+d[1]
        if 0 <= x < N and 0 <= y < N and test[x][y] == 0:
            test[x][y] = K
            heapq.heappush(heap,(K,x,y))

if __name__ == '__main__':
    N,K = map(int,sys.stdin.readline().rstrip().split(" ")) 

    test = []
    for i in range(N):
        var = list(map(int,sys.stdin.readline().rstrip().split(" ")))
        test.append(var)
    S,X,Y = map(int,sys.stdin.readline().rstrip().split(" ")) 
    
    print(solution(N,K,test,S,X,Y))