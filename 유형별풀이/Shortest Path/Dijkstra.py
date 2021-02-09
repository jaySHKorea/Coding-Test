import heapq
import sys

def get_smallest_node():
    min_value = INF
    index = 0
    for i in range(1, n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

# simple Dijkstra
def simpleD(start):
    distance[start] = 0
    visited[start] = 0
    for j in graph[start]:
        distance[j[0]] = j[1]
    for i in range(n-1):
        now = get_smallest_node()
        visited[now] = True
        for j in graph[now]:
            cost = distance[now] + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost

# faster Dijkstra - 우선순위큐
def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q:
        dist,now = heapq.heappop(q)
        if distance[now] < dist: # heap의 a까지의 최단거리보다 배열에 기록된 최단거리가 더 짧으면 스킵
            continue
        for j in graph[now]: # a에서 뻗는 노드를 본다
            cost = dist + j[1] # dist(a까지의 최단거리) + 뻗을 노드에 대한 비용
            if cost < distance[j[0]]: # 뻗을 노드까지의 총 비용이 배열에 기록된 뻗을 노드까지의 최단거리보다 짧으면 배열 갱신
                distance[j[0]] = cost # 갱신
                heapq.heappush(q, (cost, j[0])) # heap push - q에 비용,뻗을노드 push

if __name__ == '__main__':
    input = sys.stdin.readline
    INF = int(1e9)
    n,m = map(int,input().split())
    start = int(input())
    graph = [[] for i in range(n+1)]
    visited = [False] * (n+1)
    distance = [INF] * (n+1)
    for _ in range(m):
        a,b,c = map(int,input().split()) # a->b로 갈때 비용이 c
        graph[a].append(b,c)

    simpleD(start)
    dijkstra(start)
    for i in range(1,n+1):
        if distance[i] == INF:
            print("INFINITY")
        else:
            print(distance[i])