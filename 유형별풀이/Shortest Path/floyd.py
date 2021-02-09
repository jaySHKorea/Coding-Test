'''
    Floyd Algorithm
'''

INF = int(1e9)

# 노드/간선 개수
n = int(input())
m = int(input())

# 무한으로 초기화된 최단거리 배열
graph = [[INF] * (n+1) for _ in range(n+1)]

# 자기 자신으로 가는 비용 초기화
for a in range(1,n+1):
    graph[a][a] = 0

# 각 간선에 대한 정보를 입력받아 그 값으로 초기화
for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a][b] = c
    
# 점화식에 따라 플로이드 워셜 알고리즘을 수행
for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

# 수행된 결과 출력
for i in range(1,n+1):
    for j in range(1,n+1):
        if graph[i][j] == INF:
            print("INF",end=" ")
        else:
            print(graph[i][j],end=" ")
