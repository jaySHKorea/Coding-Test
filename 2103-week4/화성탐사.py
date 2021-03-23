'''
    최단 경로 03 - 화성 탐사
    당신은 화성 탐사 기계를 개발하는 프로그래머입니다. 그런데 화성은 에너지 공급원을 찾기가 힘듭니다.
    그래서 에너지를 효율적으로 사용하고자 화성 탐사 기계가 출발 지점에서 목표 지점까지 이동할 때 항상 최적의 경로를 찾도록 개발해야 합니다.

    화성탐사 기계는 NxN 크기의 2차원 공간이며, 각 칸을 지나기 위해서는 비용이 존재합니다.
    가장 위쪽 칸인 [0][0]에서 [N-1][N-1]로 이동하는 최소 비용을 출력하시오.
    이동은 상하좌우, 한번에 한칸씩 이동할 수 있습니다.
'''
import sys
import heapq
from copy import deepcopy

dirr = [(-1,0),(1,0),(0,-1),(0,1)]

def solution(N,mapp):
    answer = int(1e9)
    heap = []
    mapp2 = [[int(1e9) for _ in range(N)] for _ in range(N)]
    mapp2[0][0] = mapp[0][0]
    heapq.heappush(heap,(mapp[0][0],0,0))

    while heap:
        cost,x,y = heapq.heappop(heap)
        if x == N-1 and y == N-1:
            answer = min(answer,cost)
        for dx,dy in dirr:
            nx = x+dx
            ny = y+dy
            if 0 <= nx < N and 0 <= ny < N and mapp2[nx][ny] >= cost+mapp[nx][ny]:
                heapq.heappush(heap,(mapp[nx][ny]+cost,nx,ny))
                mapp2[nx][ny] = cost+mapp[nx][ny]
    return answer

if __name__ == '__main__':
    T = int(input())

    for i in range(T):
        N = int(input())
        mapp = []
        for j in range(N):
            var = list(map(int,sys.stdin.readline().rstrip().split(" ")))
            mapp.append(var)
        print(solution(N,mapp))