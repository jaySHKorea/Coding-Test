'''
    백준 7576 토마토

    철수의 토마토 농장에서는 토마토를 보관하는 큰 창고를 가지고 있다. 토마토는 아래의 그림과 같이 격자 모양 상자의 칸에 하나씩 넣어서 창고에 보관한다. 

    창고에 보관되는 토마토들 중에는 잘 익은 것도 있지만, 아직 익지 않은 토마토들도 있을 수 있다.
    보관 후 하루가 지나면, 익은 토마토들의 인접한 곳에 있는 익지 않은 토마토들은 익은 토마토의 영향을 받아 익게 된다.
    하나의 토마토의 인접한 곳은 왼쪽, 오른쪽, 앞, 뒤 네 방향에 있는 토마토를 의미한다.
    대각선 방향에 있는 토마토들에게는 영향을 주지 못하며, 토마토가 혼자 저절로 익는 경우는 없다고 가정한다.
    철수는 창고에 보관된 토마토들이 며칠이 지나면 다 익게 되는지, 그 최소 일수를 알고 싶어 한다.

    토마토를 창고에 보관하는 격자모양의 상자들의 크기와 익은 토마토들과 익지 않은 토마토들의 정보가 주어졌을 때,
    며칠이 지나면 토마토들이 모두 익는지, 그 최소 일수를 구하는 프로그램을 작성하라.
    단, 상자의 일부 칸에는 토마토가 들어있지 않을 수도 있다.
'''

'''
    백준 7576 토마토

    철수의 토마토 농장에서는 토마토를 보관하는 큰 창고를 가지고 있다. 토마토는 아래의 그림과 같이 격자 모양 상자의 칸에 하나씩 넣어서 창고에 보관한다. 

    창고에 보관되는 토마토들 중에는 잘 익은 것도 있지만, 아직 익지 않은 토마토들도 있을 수 있다.
    보관 후 하루가 지나면, 익은 토마토들의 인접한 곳에 있는 익지 않은 토마토들은 익은 토마토의 영향을 받아 익게 된다.
    하나의 토마토의 인접한 곳은 왼쪽, 오른쪽, 앞, 뒤 네 방향에 있는 토마토를 의미한다.
    대각선 방향에 있는 토마토들에게는 영향을 주지 못하며, 토마토가 혼자 저절로 익는 경우는 없다고 가정한다.
    철수는 창고에 보관된 토마토들이 며칠이 지나면 다 익게 되는지, 그 최소 일수를 알고 싶어 한다.

    토마토를 창고에 보관하는 격자모양의 상자들의 크기와 익은 토마토들과 익지 않은 토마토들의 정보가 주어졌을 때,
    며칠이 지나면 토마토들이 모두 익는지, 그 최소 일수를 구하는 프로그램을 작성하라.
    단, 상자의 일부 칸에는 토마토가 들어있지 않을 수도 있다.
'''
import sys

dirr = [[-1,0],[1,0],[0,-1],[0,1]]
def solution(M,N,cnt,ripped,tomato):
    answer = 0
    cumul = len(ripped)
    all = ripped

    if cumul == cnt:
        return answer
    
    # 안익은것보다 익은 것에서 부터 시작하기
    while True:
        rip = []
        for tx,ty in ripped:
            for dx,dy in dirr:
                nx = tx+dx
                ny = ty+dy
                # 조건문 복잡하게 하지 않기
                if 0 <= nx < N and 0 <= ny < M and tomato[nx][ny] == 0:
                    rip.append([tx+dx,ty+dy])
                    tomato[nx][ny] = 1
        cumul += len(rip)
        ripped = rip
        all += rip
        answer += 1
        if cumul == cnt:
            break
        elif rip == []:
            answer = -1
            break
    return answer

if __name__=='__main__':
    M,N = map(int,sys.stdin.readline().rstrip().split())
    wall = []
    ripped = []
    tomato = []
    cnt = M*N

    # 입력 & 배열 생성 한번에 하기
    for i in range(N):
        input = list(map(int,sys.stdin.readline().rstrip().split()))
        for j in range(M):
            if input[j] == -1:
                cnt -= 1
            elif input[j] == 1:
                ripped.append([i,j])
        tomato.append(input)
    print(solution(M,N,cnt,ripped,tomato))

'''
import sys

dirr = [[-1,0],[1,0],[0,-1],[0,1]]
def solution(M,N,tomato):
    answer = 0
    cnt = M*N
    ripped = []
    unripped = []

    for i in range(N):
        for j in range(M):
            if tomato[i][j] == 0:
                unripped.append([i,j])
            elif tomato[i][j] == 1:
                ripped.append([i,j])
            else:
                cnt -= 1
    
    while True:
        rip = []
        for tx,ty in unripped:
            if [tx-1,ty] in ripped or [tx+1,ty] in ripped or [tx,ty-1] in ripped or [tx,ty+1] in ripped:
                rip.append([tx,ty])
                break
        for tomato in rip:
            unripped.remove(tomato)
        if rip != []:
            ripped += rip
            answer += 1
            if len(ripped) == cnt:
                break
        else:
            answer = -1
            break
    return answer

if __name__=='__main__':
    M,N = map(int,sys.stdin.readline().rstrip().split())
    tomato = []

    for i in range(N):
        input = list(map(int,sys.stdin.readline().rstrip().split()))
        tomato.append(input)
    print(solution(M,N,tomato))
    '''