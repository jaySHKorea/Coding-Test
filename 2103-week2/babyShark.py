'''
    삼성전자 2020 상반기 공채 - 1h 30m

    아기 상어

    N x N 크기의 공간에 물고기 M마리와 아기 상어 1마리가 있습니다. 공간은 1 X 1 크기이다.

    - 한 칸에는 물고기가 최대 1마리 존재합니다.
    아기상어의 크기는 2이고, 아기상어는 1초에 상하좌우 인접한 한칸씩 이동합니다.

    모든 물고기와 상어는 자연수의 크기를 가지고 있습니다.
    아기 상어는 자신의 크기보다 큰 물고기가 있는 칸은 지나갈 수 없고, 나머지 칸은 모두 지나갑니다.
    아기상어는 자신의 크기보다 작은 물고기만 먹을 수 있습니다.
    크기가 같은 물고기는 먹을 수 없지만 지나갈 수는 있습니다.

    < 아기 상어가 이동하는 법 >
    1. 더 이상 먹을 수 있는 물고기가 공간에 없다면 아기 상어는 엄마 상어에게 도움을 요청합니다.
    2. 먹을 수 있는 물고기가 1마리라면 그 물고기를 먹으러 갑니다.
    3. 먹을 수 있는 물고기가 1마리보다 많다면, 거리가 가장 가까운 물고기를 먹으러 갑니다.
        - 거리는 아기 상어가 있는 칸에서 물고기가 있는 칸으로 이동할 때, 지나야하는 칸의 최솟값
        - 거리가 가까운 물고기가 많다면, 가장 위에 있으며 왼쪽에 있는 물고기를 먹습니다.

    아기 상어의 이동은 1초, 먹는데 시간이 걸리지 않습니다.
    아기 상어는 자신의 크기와 같은 수의 물고기를 먹을 때마다 크기가 1 증가합니다.

    아기상어는 엄마 상어에게 도움을 요청하지 않고 몇초 동안 먹을 수 있을까요?
'''

# 중요 포인트 - 계속해서 정렬된 값이 필요한 경우, sort 돌리지 말고 heapq 사용하기

import sys
from collections import deque
from copy import deepcopy
import heapq

def solution(N, space):
    answer = 0
    size = 2
    cnt = 0

    # shark 위치 찾기
    for i in range(N):
        for j in range(N):
            if space[i][j] == 9:
                shark = [i,j]
                break

    while True:
        a = bfs(shark[0],shark[1],space,size)
        if a != None:
            s,x,y = a
            
            # 원래 위치 0으로바꾸고 물고기 먹음
            space[x][y] = 0
            space[shark[0]][shark[1]] = 0
        
            # 이동시간 더하기 및 상어 위치 변경
            answer += s
            shark = [x,y]
            space[shark[0]][shark[1]] = 9 
            cnt += 1
            # 몸집 커지기
            if cnt == size:
                size += 1
                cnt = 0
        else:
            return answer

# 현재 먹을 수 있는 물고기 위치 전체 탐색 및 가까운 거리 찾기
def bfs(x, y, space, size):
    dir = [[1,0],[0,1],[-1,0],[0,-1]]
    q = deque()
    heap = []
    q.append([x,y,0])
    maps = deepcopy(space)

    # 물고기 탐색
    while q:
        x, y, point = q.popleft()
        maps[x][y] = 10

        for dx, dy, in dir: 
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]) and maps[nx][ny] != 10:
                maps[nx][ny] = 10
                if space[nx][ny] != 0 and space[nx][ny] < size: 
                    heapq.heappush(heap, [point+1,nx,ny])
                elif space[nx][ny] == size or space[nx][ny] == 0:
                    q.append([nx,ny,point+1])

    # 가능한 것 중에 가장 가까운 곳
    if heap:
        return heap[0]
    else:
        return None

if __name__ == '__main__':
    N = int(input())
    space = []
    for i in range(N):
        var = list(map(int,sys.stdin.readline().rstrip().split(" ")))
        space.append(var)

    print(solution(N,space))