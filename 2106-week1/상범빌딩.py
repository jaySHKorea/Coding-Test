'''
    백준 6593 상범빌딩
    당신은 상범 빌딩에 갇히고 말았다. 여기서 탈출하는 가장 빠른 길은 무엇일까?
    상범 빌딩은 각 변의 길이가 1인 정육면체(단위 정육면체)로 이루어져있다. 
    각 정육면체는 금으로 이루어져 있어 지나갈 수 없거나, 비어있어서 지나갈 수 있게 되어있다.
    당신은 각 칸에서 인접한 6개의 칸(동,서,남,북,상,하)으로 1분의 시간을 들여 이동할 수 있다.
    즉, 대각선으로 이동하는 것은 불가능하다.
    그리고 상범 빌딩의 바깥면도 모두 금으로 막혀있어 출구를 통해서만 탈출할 수 있다.

    당신은 상범 빌딩을 탈출할 수 있을까? 만약 그렇다면 얼마나 걸릴까?

'''

import sys
from collections import deque

dirr = [[1,0,0],[-1,0,0],[0,-1,0],[0,1,0],[0,0,-1],[0,0,1]]
def solution(L,R,C,building,start):
    answer = int(1e9)
    queue = deque()

    # 초기화
    l,r,c = start
    for dl,dr,dc in dirr:
        nl = l+dl
        nr = r+dr
        nc = c+dc
        if 0 <= nl < L and 0 <= nr < R and 0 <= nc < C and building[nl][nr][nc] == '.':
            queue.append((1,[nl,nr,nc]))
            building[nl][nr][nc] = 1
    
    # bfs
    while queue:
        step,here = queue.popleft()
        l,r,c = here

        for dl,dr,dc in dirr:
            nl = l+dl
            nr = r+dr
            nc = c+dc
            if 0 <= nl < L and 0 <= nr < R and 0 <= nc < C:
                if building[nl][nr][nc] == '.':
                    queue.append((step+1,[nl,nr,nc]))
                    building[nl][nr][nc] = step+1
                elif building[nl][nr][nc] == 'E':
                    answer = min(answer,step+1)
                elif building[nl][nr][nc] not in  ['#',"S"] and (step+1) < building[nl][nr][nc]:
                    queue.append(step+1,[nl,nr,nc])
                    building[nl][nr][nc] = step+1

    if answer == int(1e9):
        return -1
    return answer


if __name__=='__main__':
    answer = []
    while True:
        building = []
        L,R,C = map(int,sys.stdin.readline().rstrip().split())
        if L == 0 and R == 0 and C == 0:
            break
        
        for i in range(L):
            floor = []
            for j in range(R):
                input = list(sys.stdin.readline().rstrip())
                for k in range(C):
                    if input[k] == 'S':
                        start = [i,j,k]
                floor.append(input)
            input = list(sys.stdin.readline().rstrip()) # 공백줄
            building.append(floor)
        answer.append(solution(L,R,C,building,start))
    
    for ans in answer:
        if ans == -1:
            print("Trapped!")
        else:
            print("Escaped in %d minute(s)." % ans)