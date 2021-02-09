'''
    어떤 나라에는 N개의 도시가 있다. 그리고 각 도시는 보내고자 하는 메시지가 있는 경우,
    다른 도시로 전보를 보내서 해당 메시지를 전송할 수 있다. 하지만 통로가 존재해야한다.
    그리고 통로를 거쳐 메시지를 보낼 때는 일정 시간이 소요된다.

    어느날 C라는 도시에서 위급상황이 발생했고, 최대한 많은 도시로 메시지를 보내고자 한다.
    메시지는 도시 C에서 출발하여 각 도시 사이에 설치된 통로를 거쳐, 최대한 많이 퍼져나가야한다.
    각 도시의 번호와 통로가 설치되어 있는 정보가 주어졌을 때,
    도시 C에서 보낸 메시지를 받게 되는 도시의 개수는 총 몇개이며, 도시들이 모두 메시지를 받는데까지 걸리는 시간은?
'''
import sys
import heapq

def messaging(N,M,C,info):
    INF = int(1e9)

    graph = [[] for i in range(N+1)]
    distance = [INF]*(N+1)

    # 정보 삽입 i[0]->i[1]로 갈 때 비용 i[2]
    for i in info:
        graph[i[0]].append((i[1],i[2]))
    
    q = []
    heapq.heappush(q,(0,C)) # C로 가는 거리가 0
    distance[C] = 0 # 시작점 초기화
    
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist: # 갱신된 적이 있다면
            continue
        for i in graph[now]: # 현재 노드에서 갈 수 있는 곳 탐색
            cost = distance[now]+i[1] # 현재노드 거쳐서 갈때 비용 계산
            if cost < distance[i[0]]: # 거쳐서 가는게 더 가까우면
                distance[i[0]] = cost # 갱신
                heapq.heappush(q,(cost,i[0])) # push
    
    count = 0
    time = 0

    for d in distance:
        if d != INF:
            count += 1
            time = max(time,d)

    return count-1,time

if __name__ == '__main__':
    info = []
    N,M,C = map(int,input().split())
    for i in range(M):
        info.append(list(map(int,sys.stdin.readline().rstrip().split())))

    print(messaging(N,M,C,info))