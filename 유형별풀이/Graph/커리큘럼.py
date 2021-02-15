'''
    동빈이는 온라인으로 강의를 듣고 있다. 이때, 온라인 강의는 선수 강의가 있을 수 있다.
    선수 강의가 있는 강의는 선수 강의를 먼저 들어야만 해당 강의를 들을 수 있다.

    동빈이는 총 N개의 강의를 듣고자한다. 모든 강의는 1번부터 N번까지의 번호를 가진다.
    또한 동시에 여러 개의 강의를 들을 수 있다고 가정한다.
    이때 모든 강의를 수강하기까지 걸리는 최소시간을 출력하시오
'''

from collections import deque
import copy

def curriculum(N,course):
    indegree = [0]*(N+1)
    graph = [[] for i in range(N+1)]
    time = [0]*(N+1)

    for i in range(N):
        time[i+1] = course[i][0]
        for j in course[i][1:-1]:
            graph[j].append(i+1)
            indegree[i+1] += 1

    result = copy.deepcopy(time)
    q = deque()

    for i in range(1,N+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)
                result[i] = max(result[i],result[now]+time[i])
    
    return result

if __name__ == '__main__':
    course = []
    N = int(input())
    for i in range(N):
        course.append(list(map(int,input().split())))
    print(curriculum(N,course))