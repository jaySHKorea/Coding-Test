'''
    방문 판매원 A는 많은 회사가 모여 있는 공중 미래 도시에 있다. 공중 미래 도시에는 1번부터 N번까지의 회사가 있는데
    특정 회사끼리는 서로 도로를 통해 연결되어 있다. 방문 판매원 A는 현재 1번 회사에 위치해 있으며,
    X번 회사에 방문해 물건을 판매하고자 한다.

    또한 연결된 회사는 양방향으로 이동할 수 있다. 이동시간은 정확히 1이다.
    또한 방문판매원 A는 기대하던 소개팅에도 참석하고자 하는데, 상대는 K번 회사에 있다.
    A는 X번 회사에 가서 물건을 판매하기 전에 먼저 K에 찾아가 커피를 마실 예정이다. 

    첫째 줄에 전체 회사의 개수 N과 경로의 개수 M
    연결된 회사 번호가 주어짐
    X와 K가 공백으로 구분됨

    A가 K회사를 거쳐 X번 회사로 가는 최소 이동 시간을 구하라.
    X번 회사에 도달할 수 없다면 -1를 출력한다.
'''

INF = int(1e9)

# 노드/간선 개수
n,m = map(int,input().split())

# 무한으로 초기화된 최단거리 배열
graph = [[INF] * (n+1) for _ in range(n+1)]

# 자기 자신으로 가는 비용 초기화
for a in range(1,n+1):
    graph[a][a] = 0

# 각 간선에 대한 정보를 입력받아 그 값으로 초기화
for _ in range(m):
    a,b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

X,K = map(int,input().split())
    
# 점화식에 따라 플로이드 워셜 알고리즘을 수행
for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

answer = graph[1][K]+graph[K][X]

if answer >= INF:
    print(-1)
else:
    print(answer)