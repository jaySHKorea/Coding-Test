'''
    MST
    
    동물원에서 막 탈출한 원숭이 한마리가 세상을 구경하고 있는데, 마을 사람들이 도로 공사 문제로 회의 중이다.
    
    마을은 N개의 집과 그 집들을 연결하는 M개의 길로 이루어져 있다. 길은 어느 방향으로든지 다닐 수 있다.
    하지만 길마다 길을 유지하는데 드는 유지비가 있다.

    마을의 이장은 마을을 2개의 분리된 마을로 분할할 계획을 세운다. 마을을 분할할 때는 각 분리된 마을 안에 집들이 서로 연결되어야한다.
    각 분리된 마을안에 있는 임의의 두 집 사이에 경로가 항상 존재해야한다.
    그리고 마을에는 집이 하나 이상 있다.

    분리된 두 마을 사이에 있는 길들은 필요가 없으므로 없앨 수 있다. 그리고 분리된 마을 안에서도 임의의 두 집 사이에 경로가 항상 존재하게 하면서
    길을 더 없앨 수 있다. 마을의 이장은 위 조건을 만족하도록 길들을 모두 없애고, 나머지 길의 유지비의 합을 최소로 하고 싶다.
    프로그램을 작성하시오

'''
# 부모 노드 찾기
def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

# 연결하기
def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a < b: # 큰 것이 작은 것을 가리킴
        parent[b] = a
    else:
        parent[a] = b



# 최소 신장 트리를 구하고 최대 유지비의 간선을 제거
def divide(N,M,road):
    parent = [0]*(N+1)
    edges = []
    result = 0

    # 부모 테이블 자신으로 초기화
    for i in range(1,N+1):
        parent[i] = i

    # union 수행
    for i in range(M):
        a,b,cost = road[i]
        edges.append((cost,a,b))

    # 간선 비용대로 정렬
    edges.sort()
    last = 0

    for edge in edges:
        cost,a,b = edge
        if find_parent(parent,a) != find_parent(parent,b):
            union_parent(parent,a,b)
            result += cost
            last = cost
    
    return (result-last)

if __name__ == '__main__':
    road = []
    N,M = map(int,input().split())
    for i in range(M):
        road.append(list(map(int,input().split())))
    print(divide(N,M,road))