# 백준 16234 문제
'''
N×N크기의 땅이 있고, 땅은 1×1개의 칸으로 나누어져 있다.
각각의 땅에는 나라가 하나씩 존재하며, r행 c열에 있는 나라에는 A[r][c]명이 살고 있다.
인접한 나라 사이에는 국경선이 존재한다. 모든 나라는 1×1 크기이기 때문에, 모든 국경선은 정사각형 형태이다.

오늘부터 인구 이동이 시작되는 날이다.

인구 이동은 다음과 같이 진행되고, 더 이상 아래 방법에 의해 인구 이동이 없을 때까지 지속된다.

국경선을 공유하는 두 나라의 인구 차이가 L명 이상, R명 이하라면, 두 나라가 공유하는 국경선을 오늘 하루동안 연다.
위의 조건에 의해 열어야하는 국경선이 모두 열렸다면, 인구 이동을 시작한다.
국경선이 열려있어 인접한 칸만을 이용해 이동할 수 있으면, 그 나라를 오늘 하루 동안은 연합이라고 한다.
연합을 이루고 있는 각 칸의 인구수는 (연합의 인구수) / (연합을 이루고 있는 칸의 개수)가 된다. 편의상 소수점은 버린다.
연합을 해체하고, 모든 국경선을 닫는다.
각 나라의 인구수가 주어졌을 때, 인구 이동이 몇 번 발생하는지 구하는 프로그램을 작성하시오.
'''

#입력
'''
첫째 줄에 N, L, R이 주어진다. (1 ≤ N ≤ 50, 1 ≤ L ≤ R ≤ 100)
둘째 줄부터 N개의 줄에 각 나라의 인구수가 주어진다. r행 c열에 주어지는 정수는 A[r][c]의 값이다. (0 ≤ A[r][c] ≤ 100)
인구 이동이 발생하는 횟수가 2,000번 보다 작거나 같은 입력만 주어진다.
'''

#출력
# 인구 이동이 몇 번 발생하는지 첫째 줄에 출력한다.

import sys
import collections
from collections import deque

dirr = [[1,0],[-1,0],[0,1],[0,-1]] #오 왼 아래 위

def solution(N,L,R,move):
    global flag
    global move_uni
    answer = 0 # 총 인구이동 횟수
    
    while ( True ):
        answer += 1
        flag = False 
        for i in range(0,N):
            for j in range(0,N):
                if ( move_uni[i][j] == False ): # 가보지 않은 곳이라면
                    bfs(i,j) # bfs 탐색
        if ( flag == False ):break            

    return answer

# 연합인지 검사-bfs / 연합 횟수 다 더하기 / 연합 인원수 재배치 
def bfs(i,j):
    global flag, move, move_uni, dirr
    cnt = 0
    summ = 0
    # from collections import deque, append, popleft
    ch_queue = deque([])
    queue = deque([])

    move_uni[i][j] = 1 # 방문했음
    queue.append([i,j])
    ch_queue.append([i,j])

    cnt += 1
    summ += move[i][j] #연합

    while (len(queue) != 0):
        curr = queue.popleft()
        for i in range(0,4): # 4방향 탐색
            I = curr[0]+dirr[i][0]
            J = curr[1]+dirr[i][1]
            if ( I<0 or J<0 or I>=N or J>=N): continue # index over/underflow
            sub = abs(move[curr[0]][curr[1]]-move[I][J]) # 방향에 대한 차이 계산
            if ( move_uni[I][J] == False and (sub>=L and sub <=R)): # 방문한적 없고 조건 만족
                queue.append([I,J])
                ch_queue.append([I,J])
                move_uni[I][J] = True
                cnt += 1
                summ += move[I][J]
                flag = True

    if ( flag == True ): # 인구이동이 일어나야 한다
        new = int(summ/cnt)
        while (len(ch_queue) != 0):
            curr = ch_queue.popleft()
            move[curr[0]][curr[1]] = new

if __name__ == '__main__':
    flag = True # 연합이 있는지(인구이동이 있는지)
    move = [] # 입력배열

    var = list(map(int,sys.stdin.readline().rstrip().split(" ")))
    N = var[0] # N X N
    L = var[1] # L명 이상
    R = var[2] # R명 이하
    for i in range(0,N):
        move.append(list(map(int,sys.stdin.readline().rstrip().split()))) # 경사로 배열 입력 받기 list(map(int, list_a))
    move_uni = [[0 for col in range(N)] for row in range(N)] # 국가가 연합인지 아닌지 표시하는
    print(solution(N,L,R,move))