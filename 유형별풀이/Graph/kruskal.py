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

v,e = map(int,input().split())
parent = [0]*(v+1)
edges = []
result = 0

# 부모 테이블 자신으로 초기화
for i in range(1,v+1):
    parent[i] = i

# union 수행
for i in range(e):
    a,b,cost = map(int,input().split())
    edges.append((cost,a,b))

edges.sort()

for edge in edges:
    cost,a,b = edge
    if find_parent(parent,a) != find_parent(parent,b):
        union_parent(parent,a,b)
        result += cost

print(result)