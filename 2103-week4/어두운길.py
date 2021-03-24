'''
    그래프이론 03 - 어두운길 30m - MST

    한 마을은 N개의 집과 M개의 도로로 구성되어 있습니다. 각 집은 0번부터 N-1번까지의 번호로 구분됩니다.
    모든 도로에는 가로등이 구비되어 있는데, 특정 도로의 가로등을 하루 동안 켜기 위한 비용은 해당 도로의 길이와 동일하다.
    정부에서는 일부 가로등을 비활성화하되, 마을에 있는 임의의 두 집에 대하여 가로등이 켜진 도로만으로도 오갈 수 있도록 한다.
    결과적으로 일부 가로등을 비활성화하여 최대한 많은 금액을 절약하고자 한다.
    마을의 집과 도로 정보가 주어졌을 때, 일부 가로등을 비활성화하여 절약할 수 있는 최대 금액을 출력하세요.
'''
import sys
import heapq

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
def solution(N,M,road,all):
    parent = [0]*(N+1)
    edges = []
    result = 0

    # 부모 테이블 자신으로 초기화
    for i in range(1,N+1):
        parent[i] = i

    # union 수행
    for i in range(M):
        a,b,cost = road[i]
        heapq.heappush(edges,(cost,a,b))

    while edges:
        cost,a,b = heapq.heappop(edges)
        if find_parent(parent,a) != find_parent(parent,b):
            union_parent(parent,a,b)
            result += cost
    
    return (all-result)


if __name__ == '__main__':
    N,M = map(int,sys.stdin.readline().rstrip().split(" "))
    road = []
    all = 0

    for i in range(M):
        var = list(map(int,sys.stdin.readline().rstrip().split(" ")))
        road.append(var)
        all += var[2]
    print(solution(N,M,road,all))