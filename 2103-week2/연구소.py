'''
    dfs/bfs 02 20m 백준 14502

    인체에 치명적인 바이러스를 연구하던 연구소에서 바이러스가 유출되었다.
    다행히 바이러스는 아직 퍼지지 않았고, 바이러스의 확산을 막기 위해서 연구소에 벽을 세우려한다.

    연구소는 크기가 NxM인 직사각형으로 나타낼 수 있으며, 직사각형은 1x1 크기의 정사각형으로 나누어져있다.
    연구소는 빈칸, 벽으로 이루어져 있으며, 벽은 칸 하나를 가득 차지한다.

    일부 칸은 바이러스가 존재하며, 이 바이러스는 상하좌우로 인접한 빈칸으로 모두 퍼져나갈 수 있다.
    새로 세울 수 있는 벽의 개수는 3개이며, 꼭 3개를 세워야한다.

    0은 빈칸, 1은 벽, 2는 바이러스가 있는 곳이다.
'''
import sys
import itertools
import copy
from collections import deque

dirr = [[-1,0],[1,0],[0,-1],[0,1]]

# queue 미사용
def solution(N,M,map):
    answer = -1
    blank = []

    for i in range(N):
        for j in range(M):
            if map[i][j] == 0:
                blank.append((i,j))

    comb = itertools.combinations(blank,3)

    for co in comb:
        tmap = copy.deepcopy(map)
        for c in co:
            tmap[c[0]][c[1]] = 1
        for i in range(N):
            for j in range(M):
                if tmap[i][j] == 2:
                    fill(tmap,i,j)
        answer = max(answer,check(tmap))
    return answer

def solution2(N,M,map):
    answer = -1
    q = deque()
    blank = []

    for i in range(N):
        for j in range(M):
            if map[i][j] == 0:
                blank.append((i,j)) 
            elif map[i][j] == 2:
                q.append((i,j))

    # 세개의 벽을 세우는 조합
    comb = itertools.combinations(blank,3)

    for co in comb:
        queue = copy.deepcopy(q)
        tmap = copy.deepcopy(map)
        # 벽세우기
        for c in co:
            tmap[c[0]][c[1]] = 1
        # 바이러스 전파
        while queue:
            i,j = queue.popleft()
            fill(tmap,i,j)
        answer = max(answer,check(tmap))
    return answer

# dfs 
def fill(map,i,j):
    for d in dirr:
        x = i+d[0]
        y = j+d[1]
        if 0 <= x < N and 0 <= y < M and map[x][y] == 0:
            map[x][y] = 2
            fill(map,x,y)

# 안전공간 count
def check(map):
    sum = 0
    for i in range(N):
        for j in range(M):
            if map[i][j] == 0:
                sum += 1
    return sum

if __name__ == '__main__':
    N,M = map(int,sys.stdin.readline().rstrip().split(" ")) 

    mapp = []
    for i in range(N):
        var = list(map(int,sys.stdin.readline().rstrip().split(" ")))
        mapp.append(var)
    
    print(solution2(N,M,mapp))