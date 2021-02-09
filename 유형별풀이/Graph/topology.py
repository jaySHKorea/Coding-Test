from collections import deque

v,e = map(int, input().split())
indegree = [0] * (v+1)
graph = [[] for i in range(v+1)]

for _ in range(e):
    a,b = map(int,input().split())
    graph[a].append(b)
    indegree[b] += 1

def topology_sort():
    result = []
    q = deque()

    # 진입차수가 없는 노드 큐 삽입
    for i in range(1,v+1):
        if indegree[i] == 0:
            q.append(i)

    # 큐가 빌때까지
    while q:
        now = q.popleft()
        result.append(now) 

        # 현재 노드는 사라지므로 가리키던 노드들의 진입차수 마이너스
        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0: # 0이 된 노드가 있다면 큐 삽입
                q.append(i)
    
    for i in result:
        print(i,end=" ")

topology_sort()