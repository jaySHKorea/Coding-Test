'''
    dfs/bfs 06 35m 백준 18428

    N x N 크기의 복도가 있다. 복도는 1 x 1 크기의 칸으로 나누어지며, 특정한 위치에는 
    선생님/학생/장애물이 있습니다.
    
    현재 학생 몇 명이 수업 시간에 몰래 복도에 나왔는데, 복도에 나온 학생들이 선생님의 감시에 들키지 않는 것이 목표입니다.

    각 선생님은 자신의 위치에서 상하좌우 4가지 방향으로 감시를 진행합니다. 단, 복도에 장애물이 있으면 선생님은 장애물 뒤편에
    숨어 있는 학생을 볼 수 없습니다. 하지만 선생님은 시력이 매우 좋아서 아무리 멀리 있어도 장애물로 막히지 않으면 학생을 볼 수 있습니다.

    위치값은 (행,열)로 주어집니다.
    선생님은 T, 학생은 S, 장애물은 O로 표시합니다.

    학생은 복도의 빈칸 중에서 장애물을 설치할 위치를 골라, 정확히 3개의 장애물을 설치해야합니다.
    그리고 장애물을 3개 설치하고 모든 학생이 피할 수 있는지 계산해야 합니다.
    N x N 크기의 복도에서 장애물을 3개 설치해서 모든 학생이 선생님의 감시를 피할 수 있는지 출력하시오.
'''
import sys
import itertools
from collections import deque 
from copy import deepcopy

dirr = [[-1,0],[1,0],[0,-1],[0,1]]
answer = 'YES'

def solution(N,hallway):
    global answer
    teacher = deque()
    blank = deque()

    for i in range(N):
        for j in range(N):
            if hallway[i][j] == 'T':
                teacher.append((i,j))
            elif hallway[i][j] == 'X':
                blank.append((i,j))

    comb = itertools.combinations(blank,3)

    for co in comb:
        answer = 'YES'
        queue = deepcopy(teacher)
        temp = deepcopy(hallway)
        for c in co: # 벽세우기
            temp[c[0]][c[1]] = 'O'
        while queue:
            x,y = queue.popleft()
            for d in dirr:
                watch(x+d[0],y+d[1],temp,d) # 감시하기
        if answer == 'YES':
            return answer
    return 'NO'

# dfs
def watch(i,j,temp,dirr):
    global answer
    if 0 <= i < N and 0 <= j < N:
        if temp[i][j] == 'X':
            watch(i+dirr[0],j+dirr[1],temp,dirr)
        elif temp[i][j] == 'S': # 학생있으면 NO
            answer = 'NO'

if __name__ == '__main__':
    N = int(input())

    hallway = []
    for i in range(N):
        var = list(sys.stdin.readline().rstrip().split(" "))
        hallway.append(var)
    
    print(solution(N,hallway))