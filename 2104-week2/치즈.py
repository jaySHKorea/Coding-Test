'''
    https://www.acmicpc.net/problem/2638
    치즈

    NxM의 모눈종이 위에 아주 얇은 치즈가 표시되어 있다. N은 세로 격자, M은 가로 격자 수이다. 이 치즈는 냉동 보관을 해야하는데
    실내온도에 내어놓으면 공기와 접촉하여 천천히 녹는다. 이러한 모눈종이 모양의 치즈에서 각 치즈 격자의 4변 중에서 적어도 2변 이상이
    실내온도의 공기와 접촉한 것은 정확히 한시간만에 녹아 없어진다.
'''
import sys
from copy import deepcopy
sys.setrecursionlimit(10**9)
dirr = [[-1,0],[1,0],[0,-1],[0,1]]
dirr2 = [[1,0],[0,-1],[0,1]]
N,M = 0,0

def solution(N,M,cheeseMap):
    answer = 0
    cheese = cheeseList(cheeseMap)

    while cheese:
        out_check_map = onAir(0,0,deepcopy(cheeseMap))
        cheeseMap,cheese = melt(cheese,cheeseMap,out_check_map)
        answer += 1
    return answer

# 치즈
def cheeseList(cheeseMap):
    cheese = []
    for i in range(N):
        for j in range(M):
            if cheeseMap[i][j] == 1:
                cheese.append([i,j])
    return cheese

# 녹기
def melt(cheese,cheeseMap,out_check_map):
    new_map = deepcopy(cheeseMap)
    s = 0
    while True:
        if s == len(cheese):
            break
        i,j = cheese[s]
        if count(i,j,out_check_map) == True:
            new_map[i][j] = 0
            cheese.remove([i,j])
        else:
            s += 1    
    return new_map,cheese

# 바깥 공간 업데이트
def onAir(x,y,cheeseMap):
    cheeseMap[x][y] = -1
    for dx,dy in dirr2:
        nx = x+dx
        ny = y+dy
        if 0 <= nx < N and 0 <= ny < M and cheeseMap[nx][ny] == 0:
            onAir(nx,ny,cheeseMap)
    return cheeseMap

# 공기 노출된 벽 개수 세기
def count(i,j,cheeseMap):
    cnt = 0
    for dx,dy in dirr:
        nx = i+dx
        ny = j+dy
        if 0 <= nx < N and 0 <= ny < M and cheeseMap[nx][ny] == -1:
            cnt += 1
    if cnt >= 2:
        return True
    else:
        return False

if __name__=='__main__':
    N,M = map(int,sys.stdin.readline().rstrip().split())
    cheeseMap = []

    for i in range(0,N):
        input = list(map(int,sys.stdin.readline().rstrip().split()))
        cheeseMap.append(input)

    print(solution(N,M,cheeseMap))