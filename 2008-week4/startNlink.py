# 백준 14889 : 스타트와 링크
'''
오늘은 스타트링크에 다니는 사람들이 모여서 축구를 해보려고 한다. 축구는 평일 오후에 하고 의무 참석도 아니다.
축구를 하기 위해 s모인 사람은 총 N명이고 신기하게도 N은 짝수이다.
이제 N/2명으로 이루어진 스타트 팀과 링크 팀으로 사람들을 나눠야 한다.

BOJ를 운영하는 회사 답게 사람에게 번호를 1부터 N까지로 배정했고, 아래와 같은 능력치를 조사했다.
능력치 Sij는 i번 사람과 j번 사람이 같은 팀에 속했을 때, 팀에 더해지는 능력치이다.
팀의 능력치는 팀에 속한 모든 쌍의 능력치 Sij의 합이다. 
Sij는 Sji와 다를 수도 있으며, i번 사람과 j번 사람이 같은 팀에 속했을 때, 팀에 더해지는 능력치는 Sij와 Sji이다.

축구를 재미있게 하기 위해서 스타트 팀의 능력치와 링크 팀의 능력치의 차이를 최소로 하려고 한다.
위의 예제와 같은 경우에는 1, 4번이 스타트 팀, 2, 3번 팀이 링크 팀에 속하면 스타트 팀의 능력치는 6, 링크 팀의 능력치는 6이 되어서 차이가 0이 되고 이 값이 최소이다.
'''

# 첫째 줄에 N(4 ≤ N ≤ 20, N은 짝수)이 주어진다. 둘째 줄부터 N개의 줄에 S가 주어진다. 
# 각 줄은 N개의 수로 이루어져 있고, i번 줄의 j번째 수는 Sij 이다. 
# Sii는 항상 0이고, 나머지 Sij는 1보다 크거나 같고, 100보다 작거나 같은 정수이다.

# 첫째 줄에 스타트 팀과 링크 팀의 능력치의 차이의 최솟값을 출력한다.

import sys

answer = 999
member = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

#dfs
def solution(half,idx, N, S):
    global answer
    global member
    #print("idx: ")
    #print(idx)
    #print("half: ")
    #print(half)
    if ( answer == 0 ): return #최솟값 0일때 out
    elif ( half == N/2 ) : # 반만큼 select 했으면 
        score_s = 0 # start 팀의 점수
        link_s = 0 # link 팀의 점수

        for i in range(0,N):
            for j in range(i+1,N): # 조합
                if ( member[i] == member[j]): # 같은 팀인 멤버일때 서로의 능력치 add
                    #print(member)
                    if ( member[i] == 1 ) : score_s += S[i][j] + S[j][i] # start 팀일때
                    else : link_s += S[i][j] + S[j][i] # link 팀일 때

        diff = abs(score_s - link_s)
        if ( answer > diff) : answer = diff # 최소값 갱신
        return   

    elif (idx == N or N-idx < (N/2-half)) : return # idx가 N보다 커지거나 idx-half 값이 N/2보다 커지면 return

    solution(half,idx+1,N,S)
    member[idx] = 1
    solution(half+1,idx+1,N,S)
    member[idx] = 0

if __name__ == '__main__':
    N = int(sys.stdin.readline().rstrip()) # 명수 입력 받기
    S = []
    for i in range(0,N):
        S.append(list(map(int,sys.stdin.readline().rstrip().split()))) # 능력치 배열 입력 받기 list(map(int, list_a))
    solution(0,0,N,S)
    print(answer)
