'''
    구현 10 자물쇠와 열쇠

    잠겨있는 자물쇠는 격자 한칸의 크기가 1X1인 NXN 크기의 정사각 격자형태이고, 특이한 모양의 열쇠는 MXM 크기인 정사각 격자 형태이다.

    자물쇠는 홈이 파여있고, 열쇠 또한 홈과 돌기 부분이 있다. 열쇠는 회전과 이동이 가능하며, 돌기와 홈이 딱맞으면 열린다.
    자물쇠의 돌기와 열쇠의 돌기가 만나선 안된다. 자물쇠의 모든 홈을 채워 비어있는 곳이 없어야 자물쇠를 열 수 있다.

    2차원 배열인 각 key와 lock이 주어진다. 열 수 있다면 true, 없다면 false를 return 해라
'''
import copy

def solution(key, lock):
    N = len(lock)
    M = len(key)
    b = [[0 for _ in range(0,N+2*M-2)] for _ in range(0,N+2*M-2)]

    # 자물쇠 모양 삽입
    k,t = 0,0
    for i in range(M-1,N+M-1):
        t = 0
        for j in range(M-1,N+M-1):
            b[i][j] = lock[k][t]
            t += 1
        k += 1

    # 돌리면서 맞는지 검사
    for i in range(0,N+M-1):
        for j in range(0,N+M-1):
            for k in range(0,4):
                board = copy.deepcopy(b)
                if check(board,key,i,j,N) == True:
                    return True
                else:
                    key = rotate(key)
    return False

def check(board,key,i,j,N):
    M = len(key)
    y = j
    for a in range(0,M):
        j = y
        for b in range(0,M): 
            board[i][j] = board[i][j] ^ key[a][b]
            j += 1
        i += 1

    for a in range(M-1,N+M-1):
        for b in range(M-1,N+M-1):
            if board[a][b] != 1:
                return False
    return True

# 90도 회전
def rotate(key):
    M = len(key)
    newKey = [[0 for _ in range(M)] for _ in range(M)]
    for i in range(0,M):
        a = M-1
        for j in range(0,M):
            newKey[i][j] = key[a][i]
            a -= 1
    return newKey
            
print(solution([[0,0,0],[1,0,0],[0,1,1]],[[1,1,1],[1,1,0],[1,0,1]]))