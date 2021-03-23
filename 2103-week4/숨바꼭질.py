'''
    최단경로 04 - 숨바꼭질

    동빈이는 숨바꼭질을 하면서 술래로부터 잡히지 않도록 숨을 곳을 찾고 있습니다.
    동빈이는 1~N번까지의 헛간 중에서 하나를 골라 숨을 수 있으며, 술래는 항상 1번 헛간에서 출발한다.
    전체 맵에는 총 M개의 양방향 통로가 존재하며, 하나의 통로는 서로 다른 두 헛간을 연결한다.
    또한 전체 맵은 항상 어떤 헛간에서 다른 헛간으로 도달이 가능한 형태로 주어진다.

    동빈이는 1번 헛간으로부터 최단 거리가 가장 먼 헛간이 가장 안전하다고 판단하고 있습니다.
    이때 최단거리의 의미는 지나야 하는 길의 최소 개수를 의미합니다. 동빈이가 숨을 헛간의 번호를 출력하는 프로그램을 작성하세요.
'''
import sys
import heapq

def solution(N,M,mapp):
    answer = 0
    heap = []
    sol = [int(1e9) for _ in range(N+1)]
    visited = [0 for _ in range(N+1)]
    visited[1] = 1
    sol[1] = 0

    # 1에서 갈 수 있는 헛간
    for item in mapp[1]:
        heapq.heappush(heap,(item,1))

    while heap:
        now,cost = heapq.heappop(heap)
        visited[now] = 1
        if cost <= sol[now]: # 갱신
            sol[now] = cost
        for item in mapp[now]:
            if visited[item] != 1 and (item,cost+1) not in heap: # cycle 안돌도록
                heapq.heappush(heap,(item,cost+1))

    mini = max(sol[2:])
    cnt = 0
    here = 0
    for i in range(1,N+1):
        if sol[i] == mini:
            cnt += 1
            if here == 0:
                answer = i
                here += 1
    # 숨어야하는 최소 헛간 번호, 헛간거리, 같은 거리의 헛간 개수
    return answer,mini,cnt

if __name__ == '__main__':
    N,M = map(int,sys.stdin.readline().rstrip().split(" "))
    mapp = [[] for _ in range(N+1)]
    for i in range(M):
        var = list(map(int,sys.stdin.readline().rstrip().split(" ")))
        mapp[var[0]].append(var[1])
        mapp[var[1]].append(var[0])
    print(solution(N,M,mapp))