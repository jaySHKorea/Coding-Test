'''
    N X M 크기의 얼음 틀이 있다. 구멍이 뚫린 부분은 0, 칸막이가 존재하는 부분은 1
    얼음틀의 모양이 주어졌을 때, 생성되는 총 아이스크림 개수를 구하시오
'''

import sys

def makeIcecream(N,M,ice):
    answer = 0
    for i in range(N):
        for j in range(M):
            if ( dfs(i,j,N,M,ice) == True ):
                answer += 1
    return answer

def dfs(x,y,N,M,ice):
    # 현재 위치가 벗어낫는가
    if ( x < 0 or x >= N or y < 0 or y >= M):
        return False

    # 방문하지 않았다면
    if ( ice[x][y] == 0 ):
        ice[x][y] = 1
        dfs(x-1,y,N,M,ice)
        dfs(x+1,y,N,M,ice)
        dfs(x,y-1,N,M,ice)
        dfs(x,y+1,N,M,ice)
        return True
    return False
    

if __name__ == '__main__':
    ice = []
    N,M = map(int,input().split())
    for i in range(N):
        ice.append(list(map(int,input())))
    print(makeIcecream(N,M,ice))