'''
    그래프이론 04 행성 터널 - MST

    때는 2040, 우주에 왕국이 있다. 왕국은 N개의 행성으로 이루어져있다.
    이때 이 행성을 효율적으로 지배하기 위해서 행성을 연결하는 터널을 만든다.
    행성은 3차원 좌표 위의 한 점으로 생각하면 된다. 두 행성 A(xa,ya,za)와 B(xb,yb,zb)를 터널로 연결할 때 드는 비용은
    min(|xa-xb|,|ya-yb|,|za-zb|)이다.

    이때 터널을 총 N-1개로 만든다. 모든 행성을 터널로 연결하는데 필요한 최소 비용을 구하는 프로그램을 작성하세요.
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
def solution(N,road):
    parent = [0]*(N+1)
    edges = []
    answer = 0

    # 부모 테이블 자신으로 초기화
    for i in range(1,N+1):
        parent[i] = i

    # union 수행
    for i in range(N):
        xa,ya,za = road[i]
        for j in range(i+1,N):
            xb,yb,zb = road[j]
            cost = min(abs(xa-xb),abs(ya-yb),abs(za-zb))
            heapq.heappush(edges,(cost,i+1,j+1))

    while edges:
        cost,a,b = heapq.heappop(edges)
        if find_parent(parent,a) != find_parent(parent,b):
            union_parent(parent,a,b)
            answer += cost
    return answer


if __name__ == '__main__':
    N = int(input())
    road = []

    for i in range(N):
        var = list(map(int,sys.stdin.readline().rstrip().split(" ")))
        road.append(var)
    print(solution(N,road))