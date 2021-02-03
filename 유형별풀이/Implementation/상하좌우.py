'''
    N x N 지도에서 여행가가 이동한 최종 좌표를 구하시오.
'''

import sys

def travel(N,space):
    move = [[-1,0],[1,0],[0,-1],[0,1]] #상하좌우
    traveler = [0,0]

    for i in range(len(space)):
        if ( space[i] == 'U' and traveler[0] > 0):
            traveler[0] -= 1            
        elif ( space[i] == 'D' and traveler[0] < N-1):
            traveler[0] += 1
        elif ( space[i] == 'L' and traveler[1] > 0):
            traveler[1] -= 1
        elif ( space[i] == 'R' and traveler[1] < N-1):
            traveler[1] += 1

    return traveler

'''
def travel(N,space):
    x,y = 1,1
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]
    plans = ['L','R','U','D']

    for s in space:
        for i in range(len(plans)):
            if s == plans[i]:
                nx = x + dx[i]
                ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= N or ny >= N:
            continue
        x,y = nx,ny
    
    return x,y
'''

if __name__ == '__main__':
    space = []
    N = int(input())
    space = list(map(str,sys.stdin.readline().rstrip().split()))
    traveler = travel(N, space)
    print(traveler[0]+1, traveler[1]+1)