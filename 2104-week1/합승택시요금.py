'''
    2021 카카오 공채 - 합승 택시 요금 55m

    특정 노드까지 함께 합승할 수 있다고 할 때, 최소 총 비용을 구하시오.
'''

import heapq

def solution(n, s, a, b, fares):
    answer = int(1e9)

    graph = [[] for i in range(n+1)]

    # 그래프 정보
    for f in fares:
        graph[f[0]].append((f[1],f[2]))
        graph[f[1]].append((f[0],f[2]))

    # 중점을 두고 각 세 점(출발,A,B)의 거리
    for i in range(1,n+1):
        distance = dijkstra(i,n,graph)
        answer = min(distance[s]+distance[a]+distance[b],answer)

    return answer

# faster Dijkstra - 우선순위큐
def dijkstra(start,n,graph):
    INF = int(1e9)
    distance = [INF] * (n+1)
    
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

    return distance

print(solution(6,4,6,2,[[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))
print(solution(	6, 4, 5, 6, [[2, 6, 6], [6, 3, 7], [4, 6, 7], [6, 5, 11], [2, 5, 12], [5, 3, 20], [2, 4, 8], [4, 3, 9]]))

'''

def solution(n, s, a, b, fares):
    answer = 0

    point = []
    graph = [[] for i in range(n+1)]

    # 중간 지점이 될 수 잇는 노드
    for i in range(1,n+1):
        if i not in [s,a,b]:
            point.append(i)

    # 그래프 정보
    for f in fares:
        graph[f[0]].append((f[1],f[2]))
        graph[f[1]].append((f[0],f[2]))

    # 출발지~전체 노드 최소 경로값 
    way,distance = dijkstra(s,n,graph)
    start_distance = copy.deepcopy(distance)

    # 합승하지 않고 따로 가는 경우 경로와 합 구하기
    same = []
    for i in range(min(len(way[a]),len(way[b]))):
        if way[a][i] == way[b][i]:
            same.append(way[a][i])

    # 겹치는 경로가 없을 때
    if len(same) <= 1:
        answer = distance[a]+distance[b]
    # 있을 때
    else:
        answer = start_distance[same[-1]]
        way,distance = dijkstra(same[-1],n,graph)
        answer += distance[a]+distance[b]
        if same[-1] in point:
            point.remove(same[-1])

    # 특정 지점까지 합승하는 경우
    for p in point:
        temp = start_distance[p] # 합승지점
        way,distance = dijkstra(p,n,graph)
        temp += distance[a]+distance[b]
        answer = min(temp,answer)

    return answer

# faster Dijkstra - 우선순위큐
def dijkstra(start,n,graph):
    INF = int(1e9)
    distance = [INF] * (n+1)
    way = [[] for i in range(n+1)]
    
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
                temp = list(set(way[now]))
                temp.append(now)
                way[j[0]] = temp
                heapq.heappush(q, (cost, j[0])) # heap push - q에 비용,뻗을노드 push

    for i in range(1,n+1):
        if way[i] != []:
            way[i].append(i)
    return way,distance
'''