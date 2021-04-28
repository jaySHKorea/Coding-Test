'''
    게임 개발자인 베로니는 개발 연습을 위해 간단한 카드 짝맞추기 보드 게임을 개발해보려고 합니다.

    게임이 시작되면 화면에는 카드 16장이 뒷면을 위로하여 4x4로 표시됩니다.
    8가지의 캐릭터 그림이 그려진 카드가 2장씩 무작위로 배치되어 있습니다.

    유저가 카드 2장을 선택하여 앞면으로 뒤집었을 때 같은 그림이 그려진 카드면, 해당 카드는 게임 화면에서 사라집니다.
    아니면 다시 뒷면으로 뒤집힙니다. 이와 같은 방법으로 모든 카드를 화면에서 사라지게 하면 게임이 종료됩니다.

    유저는 커서를 이동합니다. 방향키(1칸이동)를 누르거나, ctrl+방향키(누른 키 방향의 가장 가까운 카드로 한번에 이동, 카드가 없다면 마지막 칸으로 이동)

    커서가 위치한 카드를 뒤집기 위해서는 enter 키를 입력합니다.
    입력시 2장이 뒤집힐 때까지 기다리고, 같으면 사라지고, 아니면 다시 뒤집힙니다.

    카드의 짝을 맞춰 몇 장 제거된 상태에서 카드 앞면의 그림을 알고 있다면, 남은 카드를 모두 제거하는데 필요한 키 조작 횟수의 최솟값을 구하세요.
'''
from collections import deque
from copy import deepcopy

dirr = [-1,1] # 상하좌우
answer = 0
def solution(board, r, c):
    global answer
    cards = []
    for i in range(4):
        for j in range(4):
            if board[i][j] != 0:
                cards.append((board[i][j],i,j))

    for card in cards:
        dfs(card,board) 
    return answer

def dfs(r,c,card,cards,board):
    global answer
    n_cards = deepcopy(cards)
    n_board = deepcopy(board)
    card_num,nr,nc = card

    while r != nr and c != nc:
        if r == nr and c == nc: # 현재 자리에 카드가
            answer += 1 # enter
            break
        # 같은 행 혹은 열
        if r == nr:
            answer += 1
            if c < nc: # 우 방향 이동
                r,c = ctrldir(r,c,1,0,board)
            else: # 좌 방향 이동
                r,c = ctrldir(r,c,0,0,board)
        elif c == nc:
            answer += 1
            if r < nr: # 아래 방향 이동
                r,c = ctrldir(r,c,1,1,board)
            else:
                r,c = ctrldir(r,c,0,1,board)
        # 둘 다 다를 때
        else:
            # x 맞추기
            dist = abs(nr-r)
            if r < nr:
                mr,mc = ctrldir(r,c,1,1,board)
            else:
                mr,mc = ctrldir(r,c,0,1,board)
            if r == mr:
                answer += 1
                r = mr
            else:
                r = mr

    q = deque()

def ctrldir(r,c,dir,rc,board):
    if rc == 0: # 좌우 움직임
        c += dirr[dir]
        while 0 <= c < 4:
            if board[r][c] != 0:
                return r,c
            c += dirr[dir]
        return r,c+dirr[(dir+1)%2]
    else: # 상하 움직임
        r += dirr[dir]
        while 0 <= r < 4:
            if board[r][c] != 0:
                return r,c
            r += dirr[dir]
        return r+dirr[(dir+1)%2],c

print(solution([[1,0,0,3],[2,0,0,0],[0,0,0,2],[3,0,1,0]],1,0))