'''
    그래프이론 05 - 최종순위 ( 위상정렬 응용 )

    올해 icm-icpc 대전 예선에 총 n개의 팀이 참가했다. 팀은 1번부터 n번까지 번호가 매겨져 있다.
    놀랍게도 올해 참가하는 팀은 작년에 참가했던 팀과 동일하다.

    올해 예선 본부는 최종 순위를 발표하지 않기로 했다. 그 대신에 작년에 비해서 상대적으로 순위가 바뀐 팀의 목록만 발표하려한다.
    
    이 정보만 가지고 올해 최종 순위를 만들어보려고 한다. 작년 순위와 상대적인 순위가 바뀐 모든 팀의 목록이 주어졌을 때,
    올해 순위를 만드는 프로그램을 작성하세요.

    확실한 올해 순위를 만들 수 없는 경우가 있을 수도 있고, 일관성이 없는 잘못된 정보일 수도 있습니다. 이 두경우도 모두 찾아내야 합니다.
'''
import sys
from collections import deque

def solution(n,lyear,m,relative):
    answer = []
    is_cycle,is_ambi = False,False
    indegree = [0] * (n+1)
    graph = [[] for i in range(n+1)]
    q = deque()

    # 1. 진입 차수 배열 생성
    for i in range(n):
        for j in range(i+1,n):
            graph[lyear[j]].append(lyear[i])
            indegree[lyear[i]] += 1
    
    # 2. 순위 바뀐 순서쌍 간선 방향 변경
    for a,b in relative:
        if b in graph[a] and a not in graph[b]:
            indegree[b] -= 1
            graph[a].remove(b)
            indegree[a] += 1
            graph[b].append(a)
        else:
            indegree[a] -= 1
            graph[b].remove(a)
            indegree[b] += 1
            graph[a].append(b)

    # 진입차수가 0인 것들 큐에 추가
    for i in range(1,n+1):
        if indegree[i] == 0:
            q.append(i)

    # 3. topology sort
    for i in range(n):
        # 진입차수가 0인게 없는 (일관성 없는 경우 2)
        if len(q) == 0:
            is_cycle = True
            break

        # 확실한 순위를 알 수 없는 경우
        if len(q) >= 2:
            is_ambi = True
            break
        now = q.popleft()
        answer.append(now) 

        # 현재 노드는 사라지므로 가리키던 노드들의 진입차수 마이너스
        for j in graph[now]:
            indegree[j] -= 1
            if indegree[j] == 0: # 0이 된 노드가 있다면 큐 삽입
                q.append(j)

    if is_cycle:
        print("IMPOSSIBLE")
    elif is_ambi:
        print("?")
    else:
        answer.reverse()
        for a in answer:
            print(a,end=' ')
        print()

if __name__ == '__main__':
    pp = []
    N = int(sys.stdin.readline().rstrip())

    for i in range(N):
        relative = []
        n = int(sys.stdin.readline().rstrip())
        lyear = list(map(int,sys.stdin.readline().rstrip().split(" ")))
        m = int(sys.stdin.readline().rstrip())
        for j in range(m):
            relative.append(list(map(int,sys.stdin.readline().rstrip().split(" "))))
        solution(n,lyear,m,relative)