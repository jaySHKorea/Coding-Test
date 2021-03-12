'''
    dfs/bfs 08 2020 카카오 신입공채 1차 - 2h

    로봇개발자 무지는 한달 앞으로 다가온 카카오배 로봇경진대회에 출품할 로봇을 준비중이다.

    준비중인 로봇은 2X1 크기의 로봇으로 무지는 0과 1로 이루어진 NxN 크기의 지도에서
    2x1 크기의 로봇을 움직여 (N,N) 위치까지 이동할 수 있도록 프로그래밍을 하려한다.

    로봇이 이동하는 지도는 가장 왼쪽, 상단의 좌표를 (1,1)로 하며 지도 내에 표시된 숫자 0은 빈칸, 1은 벽을 나타낸다.
    로봇은 벽이 있는 칸 또는 지도 밖으로는 이동할 수 없다.
    로봇은 처음 좌표 (1,1)에서 가로방향으로 놓여있고, 아뒤 구분없이 움직일 수 있다.

    로봇은 항상 두칸을 차지하며, 조건에 따라 회전이 가능한데, 항상 90도씩 회전을 합니다.
    회전은 1초가 걸립니다. 축으로 부터 대각선 칸에 벽이 없어야합니다.

    0과 1로 이루어진 지도가 주어질 때, 로봇이 (N,N)까지 이동하는 최소 시간을 구하시오.
'''

from collections import deque
import heapq

'''
dirr = [[1,0],[-1,0],[0,-1],[0,1]]
def solution(board):
    answer = 0

    heap = []
    N = len(board)
    shortest = [[int(1e9) for _ in range(N+1)] for _ in range(N+1)]
    shortest[1][1] = 0
    shortest[1][2] = 0
    heapq.heappush(heap,(0,(1,1),(1,2)))

    while heap:
        c,tail,head = heapq.heappop(heap)
        cost = c+1

        for d in dirr:
            h = (head[0]+d[0],head[1]+d[1])
            t = (tail[0]+d[0],tail[1]+d[1])
            if 0 < h[0] <= N and 0 < h[1] <= N and 0 < t[0] <= N and 0< t[1] <= N and board[h[0]-1][h[1]-1] == 0 and board[t[0]-1][t[1]-1] == 0  and ( cost <= shortest[h[0]][h[1]] or cost <= shortest[t[0]][t[1]]):
                if cost < shortest[h[0]][h[1]]:
                    shortest[h[0]][h[1]] = cost
                if cost < shortest[t[0]][t[1]]:
                    shortest[t[0]][t[1]] = cost
                heapq.heappush(heap,(cost,t,h))

        # 로봇이 가로방향일 때
        if head[0] == tail[0]:
            # 위로 90도 회전
            x = head[0]-1
            y = head[1]
            if 0 < x <= N and 0 < y <= N and board[x-1][y-1] == 0 and board[x-1][tail[1]-1] == 0 and cost <= shortest[x][y]:
                shortest[x][y] = cost
                heapq.heappush(heap,(cost,(x,y),head))
            # 아래로 90도 회전
            x = head[0]+1
            y = head[1]
            if 0 < x <= N and 0 < y <= N and board[x-1][y-1] == 0 and board[x-1][tail[1]-1] == 0 and cost <= shortest[x][y]:
                shortest[x][y] = cost
                heapq.heappush(heap,(cost,head,(x,y)))
            # 위로 90도 회전
            x = tail[0]-1
            y = tail[1]
            if 0 < x <= N and 0 < y <= N and board[x-1][y-1] == 0 and board[x-1][head[1]-1] == 0 and cost <= shortest[x][y]:
                shortest[x][y] = cost
                heapq.heappush(heap,(cost,(x,y),tail))
            # 아래로 90도 회전
            x = tail[0]+1
            y = tail[1]
            if 0 < x <= N and 0 < y <= N and board[x-1][y-1] == 0 and board[x-1][head[1]-1] == 0 and cost <= shortest[x][y]:
                shortest[x][y] = cost
                heapq.heappush(heap,(cost,tail,(x,y)))
        # 로봇이 세로방향일 때
        elif head[1] == tail[1]:
            # 왼쪽 90도 회전
            x = head[0]
            y = head[1]-1
            if 0 < x <= N and 0 < y <= N and board[x-1][y-1] == 0 and board[tail[0]-1][y-1] == 0 and cost <= shortest[x][y]:
                shortest[x][y] = cost
                heapq.heappush(heap,(cost,(x,y),head))
            # 오른쪽 90도 회전
            x = head[0]
            y = head[1]+1
            if 0 < x <= N and 0 < y <= N and board[x-1][y-1] == 0 and board[tail[0]-1][y-1] == 0 and cost <= shortest[x][y]:
                shortest[x][y] = cost
                heapq.heappush(heap,(cost,head,(x,y)))
            # 좌측 90도 회전
            x = tail[0]
            y = tail[1]-1
            if 0 < x <= N and 0 < y <= N and board[x-1][y-1] == 0 and board[head[0]-1][y-1] == 0 and cost <= shortest[x][y]:
                shortest[x][y] = cost
                heapq.heappush(heap,(cost,(x,y),tail))
            # 우측 90도 회전
            x = tail[0]
            y = tail[1]+1
            if 0 < x <= N and 0 < y <= N and board[x-1][y-1] == 0 and board[head[0]-1][y-1] == 0 and cost <= shortest[x][y]:
                shortest[x][y] = cost
                heapq.heappush(heap,(cost,tail,(x,y)))

    return shortest[N][N]
'''

from collections import deque

dirr = [[-1,0],[1,0],[0,-1],[0,1]]
def can_move(tail, head, new_board):
    X, Y = 0, 1
    cand = []

    # 상하좌우
    for dx, dy in dirr:
        nxt1 = (tail[X] + dx, tail[Y] + dy)
        nxt2 = (head[X] + dx, head[Y] + dy)
        if new_board[nxt1[X]][nxt1[Y]] == 0 and new_board[nxt2[X]][nxt2[Y]] == 0:
            cand.append((nxt1, nxt2))
    # 회전
    if tail[X] == head[X]: # 가로방향 일 때
        for d in [-1,1]:
            if new_board[tail[X]+d][tail[Y]] == 0 and new_board[head[X]+d][head[Y]] == 0: # 두칸 모두 비어있어야 가능
                cand.append((tail, (tail[X]+d, tail[Y])))
                cand.append((head, (head[X]+d, head[Y])))
    else: # 세로 방향 일 때
        for d in [-1,1]:
            if new_board[tail[X]][tail[Y]+d] == 0 and new_board[head[X]][head[Y]+d] == 0: 
                cand.append(((tail[X], tail[Y]+d), tail))
                cand.append(((head[X], head[Y]+d), head))
                
    return cand

def solution(board):
    N = len(board)
    new_board = [[1 for _ in range(N+2)] for _ in range(N+2)]
    for i in range(N):
        for j in range(N):
            new_board[i+1][j+1] = board[i][j]

    que = deque([((1, 1), (1, 2), 0)])
    confirm = set([((1, 1), (1, 2))])

    while que:
        tail, head, count = que.popleft()
        if tail == (N, N) or head == (N, N):
            return count
        for nxt in can_move(tail, head, new_board):
            if nxt not in confirm:
                que.append((*nxt, count+1))
                confirm.add(nxt)

print(solution([[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]))
print(solution([[0,0],[0,0]]))