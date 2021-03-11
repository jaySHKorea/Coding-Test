'''
    dfs/bfs 01 30m 백준 18352

    어떤 나라에는 1~N번까지의 도시와 M개의 단방향 도로가 존재한다. 모든 도로의 거리는 1이다.
    이때 특정한 도시 X로부터 출발하여 도달할 수 있는 모든 도시 중에서, 최단 거리가 정확히 K인 모든 도시의 번호를 출력하는 프로그램을 작성하세요.
    또한 출발 도시 X에서 출발 도시 X로 가는 최단 거리는 항상 0이라고 가정합니다.
'''

# 다익스트라 똑바로 구현할 것!

from collections import deque
import sys
import heapq

def solution(info,K,X,N):
    q = []
    shortest = [int(1e9) for _ in range(N+1)]

    shortest[X] = 0
    heapq.heappush(q,(0,X)) # cost 0, 시작점 X
    while q:
        dist,now = heapq.heappop(q)
        if shortest[now] < dist: # cost가 now의 최단거리보다 크면
            continue
        for node in info[now]: # now에서 뻗는 점들 검사
            point = dist+1 # 한칸 더
            if point < shortest[node]: # 현재 포인트가 node의 최단거리보다 짧으면
                shortest[node] = point
                heapq.heappush(q,(point,node))

    if K in shortest:
        for i,a in enumerate(shortest):
            if a == K:
                print(i)
    else:
        print(-1)

if __name__ == '__main__':
    N,M,K,X = map(int,sys.stdin.readline().rstrip().split(" ")) #도시개수, 도로개수, 거리정보, 출발도시번호 X

    info = [[] for _ in range(300001)]
    for i in range(M):
        var = list(map(int,sys.stdin.readline().rstrip().split(" ")))
        info[var[0]].append(var[1])
    
    solution(info,K,X,N)