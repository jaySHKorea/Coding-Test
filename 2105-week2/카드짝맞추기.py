'''
    
    카드 짝맞추기 - bfs + dfs
    
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

d = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def end_game(b):
    if b.count("0") == 16:
        return True
    return False

def remove_element(b, e):
    b = b.replace(e, "0")
    return b

def move(b, y, x, dy, dx):
    ny, nx = y + dy, x + dx
    if ny >= 0 and ny < 4 and nx >= 0 and nx < 4 and b[ny * 4 + nx] == "0": # 갈 수 있고 0일때 
        return move(b, ny, nx, dy, dx)
    else:
        if ny >= 0 and ny < 4 and nx >= 0 and nx < 4: # 여기가 ctrl이동으로 올 수 있는 마지막
            return (ny, nx)
        else:
            return (y, x) # ctrl 눌러도 내 자리로 돌아온다

def solution(board, r, c):
    answer = 0
    b = ""
    for i in range(4):
        for j in range(4):
            b += str(board[i][j])
    q = deque([])

    cnt = 0
    enter = -1 # enter을 클릭했던 위치
    q.append((r, c, b, cnt, enter))
    s = set()

    while q:
        y, x, b, c, e = q.popleft()
        pos = 4 * y + x

        if (y, x, b, e) in s: # 같은 상태(board)를 가지고 온 적이 있는 자리다
            continue
        s.add((y, x, b, e))

        if end_game(b):
            return c

        # 4 방향 이동
        for (dy, dx) in d:
            ny, nx = y + dy, x + dx
            if ny >= 0 and ny < 4 and nx >= 0 and nx < 4:
                q.append((ny, nx, b, c+1, e))

        # Ctrl + 4 방향 이동
        for (dy, dx) in d:
            ny, nx = move(b, y, x, dy, dx)
            if ny == y and nx == x: # 눌러도 제자리다
                continue
            q.append((ny, nx, b, c+1, e))

        # enter를 하는 경우
        if b[pos] != 0:
            if e == -1: # 해당 숫자의 카드를 처음 뒤집는다
                n_e = pos
                q.append((y, x, b, c+1, n_e))
            else:
                if e != pos and b[e] == b[pos]: # 같은 자리의 카드가 아니고, 같은 숫자의 카드 일때
                    b = remove_element(b, b[e])
                    q.append((y, x, b, c+1, -1))

    return answer

print(solution([[1,0,0,3],[2,0,0,0],[0,0,0,2],[3,0,1,0]],1,0))