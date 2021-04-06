'''
    삼성전자 공채 - 청소년 상어

    4 X 4 크기의 공간이 있고, 크기가 1 X 1인 정사각형으로 나누어져있다.
    공간의 각 칸은 (x,y)로 표현하며, 한칸에는 물고기가 1마리 있고, 각 물고기는 번호와 방향을 가집니다.
    번호는 1보다 크거나 같고, 16보다 작거나 같은 자연수이며, 두 물고기가 같은 번호를 갖는 경우는 없습니다.
    방향은 8가지 방향(상하좌우,대각선) 중 하나 입니다.

    오늘은 청소년 상어가 이 공간에 들어가 물고기를 먹으려고 합니다. 청소년 상어는 (0,0)에 있는 물고기를 먹고
    (0,0)에 들어가는데, 상어의 방향은 (0,0)에 있던 물고기의 방향과 같습니다.

    < 물고기의 이동 >
    물고기는 번호가 작은 물고기부터 순서대로 이동합니다.
    물고기는 한 칸을 이동할 수 있고, 이동할 수 있는 칸은 빈칸과 다른 물고기가 있는 칸입니다.
    이동할 수 없는 칸은 상어가 있거나 공간의 경계를 넘는 칸입니다.
    물고기는 이동할 수 있는 칸을 찾을때까지 반시계 방향으로 회전합니다.
    물고기는 이동할 수 있는 칸이 없으면 이동을 하지 않습니다. 다른 물고기가 있는 칸으로 이동하면 서로의 위치를 바꿉니다.

    < 상어의 이동 >
    상어는 방향에 있는 칸으로 이동할 수 있고, 한 번에 여러 칸을 이동할 수 있습니다.
    상어가 물고기가 있는 칸으로 이동했다면, 그 칸에 있는 물고기를 먹고, 그 물고기의 방향을 가집니다.
    이동하는 중에 지나가는 칸에 있는 물고기는 먹지 않으며, 물고기가 없는 칸으로 이동할 수 없습니다.
    상어가 이동할 수 있는 칸이 없으면 공간에서 벗어나 집으로 돌아갑니다.
    상어가 이동한 후에는 다시 물고기가 이동하며, 과정이 반복됩니다.
'''
# 물고기 번호에 대해 그리디 불가능, dfs or bfs 사용해야함

import sys
import copy

dirr = [[-1,0],[-1,-1],[0,-1],[1,-1],[1,0],[1,1],[0,1],[-1,1]]
answer = 0

def solution(move,fishes):
    global answer
    fishes = sorted(fishes,key=lambda x:x[0])
    shark = (1,1,move[1][1][1]) # x,y,방향
    eat(shark,fishes,move[1][1][0],0,move)
    return answer

# 물고기 먹기
def eat(shark,fishes,i,summ,move):
    global answer
    n_move = copy.deepcopy(move)
    n_fishes = copy.deepcopy(fishes)
    n_shark = shark

    summ += i # 최대 번호 합
    can = [] # 상어가 이동할 수 있는 곳
    x = n_shark[0]
    y = n_shark[1]
    shark_dir = n_shark[2]-1
    n_fishes[i-1] = [i,0,0,0] # 현재 위치의 물고기를 먹기
    n_move[x][y] = (0,0) # 배열에서 물고기 먹음 처리

    # 물고기들의 이동
    rotate(n_shark,n_fishes,n_move)

    while True:
        nx = x+dirr[shark_dir][0]
        ny = y+dirr[shark_dir][1]
        if 0 < nx < 5 and 0 < ny < 5:
            if n_move[nx][ny] != (0,0): # 빈칸이 아닐 때
                can.append((nx,ny,n_move[nx][ny][0],n_move[nx][ny][1]))
            x = nx
            y = ny
        else:
            break
    
    # dfs
    if can:
        for c in can: 
            n_shark = (c[0],c[1],c[3])
            eat(n_shark,n_fishes,c[2],summ,n_move)
    # 이동 할 수 있는 곳이 없을 때, 갱신
    else:
        answer = max(answer,summ)

# 물고기 이동
def rotate(shark,fishes,move):
    for fish in fishes:
        if fish[1] == 0: # 잡아먹힌 물고기일 떄
            continue

        fish_num = fish[0]
        fish_dir = fish[1]-1
        x = fish[2]
        y = fish[3]
    
        while True:
            nx = x + dirr[fish_dir][0]
            ny = y + dirr[fish_dir][1]
            if 0 < nx < 5 and 0 < ny < 5 and shark != (nx,ny,shark[2]): # 상어가 아닌 자리일 떄
                new_fish_num = move[nx][ny][0]
                # swap
                move[x][y] = move[nx][ny]
                move[nx][ny] = (fish_num,fish_dir+1)
                # 방향,좌표 갱신
                fishes[fish_num-1] = [fish_num,fish_dir+1,nx,ny]  
                # 빈칸이 아닐 때
                if move[x][y] != (0,0):   
                    fishes[new_fish_num-1][2] = x
                    fishes[new_fish_num-1][3] = y  
                break
            fish_dir = (fish_dir+1)%8
    
if __name__=='__main__':
    move = [[0 for _ in range(5)] for _ in range(5)]
    fishes = []

    for i in range(1,5):
        input = list(map(int,sys.stdin.readline().rstrip().split()))
        for j in range(1,5):
            fish_num = input[(j-1)*2]
            fish_dir = input[(j-1)*2+1]
            move[i][j] = (input[(j-1)*2],input[(j-1)*2+1])
            fishes.append([fish_num,fish_dir,i,j])
            #heapq.heappush(fishes,(fish_num,fish_dir,i,j))
    print(solution(move,fishes))


'''
dirr = [[-1,0],[-1,-1],[0,-1],[1,-1],[1,0],[1,1],[0,1],[-1,1]]
answer = 0

def solution(move,fishes):
    global answer
    fishes = sorted(fishes,key=lambda x:x[0])
    shark = (1,1,move[1][1][1]) # x,y,방향
    answer += move[1][1][0]
    fishes[move[1][1][0]-1] = [move[1][1][0],0,0,0]
    move[1][1] = (0,0)
    while True:

        # 물고기의 이동
        for fish in fishes:
            if fish[1] == 0:
                continue
            rotate(fish,shark,fishes)
        # 물고기 먹기
        shark = eat(move,shark,fishes)
        if shark == False:
            break
    return answer

# 물고기 먹기
def eat(move,shark,fishes):
    global answer
    can = []
    x = shark[0]
    y = shark[1]
    shark_dir = shark[2]-1

    while True:
        nx = x+dirr[shark_dir][0]
        ny = y+dirr[shark_dir][1]
        if 0 < nx < 5 and 0 < ny < 5:
            if move[nx][ny] != (0,0):
                can.append((nx,ny,move[nx][ny][0],move[nx][ny][1]))
                x = nx
                y = ny
        else:
            break
    
    if can:
        can = sorted(can,reverse=True,key=lambda x:x[2])
        toeat = can[0]
        shark = (toeat[0],toeat[1],toeat[3]) # shark 정보 갱신
        fishes[toeat[2]-1] = [toeat[2],0,0,0]
        answer += toeat[2]
        move[toeat[0]][toeat[1]] = (0,0) # 배열에서 물고기 삭제
        return shark
    else:
        return False

# 물고기 이동
def rotate(fish,shark,fishes):
    fish_num = fish[0]
    fish_dir = fish[1]-1
    x = fish[2]
    y = fish[3]
    
    while True:
        nx = x + dirr[fish_dir][0]
        ny = y + dirr[fish_dir][1]
        if 0 < nx < 5 and 0 < ny < 5 and shark != (nx,ny,shark[2]):
            new_fish_num = move[nx][ny][0]
            move[x][y],move[nx][ny] = move[nx][ny],move[x][y]
            fishes[fish_num-1][2] = nx
            fishes[fish_num-1][3] = ny
            if move[x][y] != (0,0):   
                fishes[new_fish_num-1][2] = x
                fishes[new_fish_num-1][3] = y
            
            break
        fish_dir = (fish_dir+1)%8
'''