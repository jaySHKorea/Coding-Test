'''
    서로소집합
    
    학교에서 학생들에게 0번부터 N번까지의 번호를 부여했다. 처음에는 모든 학생이 서로 다른 팀으로 구분되어 총 N+1개의 팀이 존재한다.
    이때, 선생님은 '팀 합치기'와 '같은 팀 여부 확인' 연산을 사용할 수 있다.

    선생님이 M개의 연산을 수행할 수 있을 때, '같은 팀 여부 확인' 연산에 대한 연산 결과를 출력하는 프로그램을 작성하시오
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

def make_team(N,M,stu):
    parent = [0]*(N+1)

    # 부모 테이블 자신으로 초기화
    for i in range(N+1):
        parent[i] = i

    # union 수행
    for i in range(M):
        oper,a,b = stu[i]
        if oper == 0:
            union_parent(parent,a,b)
        elif oper == 1: 
            if find_parent(parent,a) == find_parent(parent,b):
                print('YES')
            else:
                print('NO')

if __name__ == '__main__':
    stu = []
    N,M = map(int,input().split())
    for i in range(M):
        stu.append(list(map(int,input().split())))
    make_team(N,M,stu)