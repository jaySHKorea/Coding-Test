'''
    구현-11

    Dummy라는 도스 게임이 있습니다. 이 게임에는 뱀이 나와서 기어 다니는데, 사과를 먹으면 뱀의 길이가 늘어납니다.
    뱀이 이리저리 기어 다니다가 벽 또는 자기 자신의 몸과 부딪히면 게임이 끝납니다.

    게임은 N X N 정사각 보드 위에서 진행되고, 몇몇 칸에는 사과가 놓여져있습니다.
    보드의 상하좌우 끝에는 벽이 있습니다. 게임을 시작할 때 뱀은 맨위 맨 좌측에 있으며 길이는 1입니다.
    뱀은 처음에 오른쪽을 향합니다.

    뱀은 초마다 이동하며 다음 규칙을 따릅니다.
    1. 먼저 뱀은 몸길이를 늘려 다음 칸에 위치시킵니다.
    2. 이동한 칸에 사과가 있다면 그 칸에 있던 사과는 없어지고 꼬리는 움직이지 않습니다.
    3. 만약 이동한 칸에 사과가 없다면 몸길이를 줄여서 꼬리가 위치한 칸을 비워줍니다. 몸길이는 변하지 않습니다.

    사과의 위치와 뱀의 이동 경로가 주어집니다. 게임이 몇 초 안에 끝나는지 계산하세요
'''

# 시작과 끝 정보가 필요한 경우 queue를 사용할 것!!!! 
import sys
from collections import deque

dirr = [[0,1],[1,0],[0,-1],[-1,0]]

def solution(board,move):
    N = len(board)
    answer = 0
    
    time,where = move.popleft() # head 이동 방향 변환점
    now_dir = [0,0] # head 위치
    go = 0 # 이동 방향
    
    # 초기화
    board[0][0] = 2
    snake = deque()
    snake.append((0,0))
    
    while True:
        # 초 카운트
        answer += 1

        # 이동
        now_dir[0] += dirr[go][0]
        now_dir[1] += dirr[go][1]
        
        # 벽이나 자기자신인지 검사
        if ( now_dir[0] < 0 or now_dir[0] >= N or now_dir[1] < 0 or now_dir[1] >= N or board[now_dir[0]][now_dir[1]] == 2): 
            return answer

        # 사과가 아니라면 꼬리 당겨주기
        if ( board[now_dir[0]][now_dir[1]] != 1):
            tail_x,tail_y = snake.popleft()
            board[tail_x][tail_y] = 0
            
        # 이동 및 머리 삽입
        board[now_dir[0]][now_dir[1]] = 2
        snake.append((now_dir[0],now_dir[1]))
        
        # 방향회전
        if ( time == answer ):
            if ( where == 'L'):
                go = (go+3)%4
            else:
                go = (go+1)%4
            if move:
                time,where = move.popleft()

if __name__ == '__main__':
    N = int(input()) # 2~100 작음
    board = [[0 for _ in range(N)] for _ in range(N)]
    K = int(input()) # 0~100
    for i in range(K):
        var = list(map(int,sys.stdin.readline().rstrip().split(" ")))
        board[var[0]-1][var[1]-1] = 1
    L = int(input())

    move = deque()
    for i in range(L):
        var = list(sys.stdin.readline().rstrip().split(" "))
        move.append((int(var[0]),var[1])) # L은 왼쪽 D는 오른쪽 90도 회전
    print(solution(board,move))