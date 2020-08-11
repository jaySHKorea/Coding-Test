# 백준 14501번 문제 : DP, 브루트포스
# 퇴사
"""
상담원으로 일하고 있는 백준이는 퇴사를 하려고 한다.
오늘부터 N+1일째 되는 날 퇴사를 하기 위해서, 남은 N일 동안 최대한 많은 상담을 하려고 한다.
백준이는 비서에게 최대한 많은 상담을 잡으라고 부탁을 했고, 비서는 하루에 하나씩 서로 다른 사람의 상담을 잡아놓았다.
각각의 상담은 상담을 완료하는데 걸리는 기간 Ti와 상담을 했을 때 받을 수 있는 금액 Pi로 이루어져 있다.
N = 7인 경우에 다음과 같은 상담 일정표를 보자.
"""

# 입력
"""
첫째 줄에 N (1 ≤ N ≤ 15)이 주어진다.
둘째 줄부터 N개의 줄에 Ti와 Pi가 공백으로 구분되어서 주어지며, 1일부터 N일까지 순서대로 주어진다. (1 ≤ Ti ≤ 5, 1 ≤ Pi ≤ 1,000)
"""

# 출력
"""
첫째 줄에 백준이가 얻을 수 있는 최대 이익을 출력한다.
"""

#DP
"""
작은문제의 반복이 일어날 때, 모든 작은 문제는 1번만 푼다.
같은문제를 구할때는 답이 같다.
Bottom-up(상향식 계산)과 Top-down(memozation)
"""

#점화식 찾기
"""
max(dp[i],dp[j])
max(dp[i],dp[j]+sch[j][1](P값))
"""
import sys

def solution(N, sch):
    dp = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    answer = 0
    for i in range(0,N+1): # N+1까지
        for j in range(0,i): #N까지
            dp[i] = max(dp[i],dp[j]) # 지금까지 쌓아온 dp값 중에 max값 저장
            if ( j + sch[j][0] == i): # 쌓아온 dp 값에 상담 일수가 맞아떨어지는 것
                dp[i] = max(dp[i],dp[j]+sch[j][1]) # 쌓아온 dp에 또 쌓기
        answer = max(answer,dp[i]) # 일차가 지날때마다 높은 dp값으로 갱신
    return answer

if __name__ == '__main__':
    N = int(sys.stdin.readline().rstrip()) # 백준 python 입력 받기, rstrip은 공백처리
    sch = []
    for i in range(1,N+1):
        a = sys.stdin.readline().rstrip().split() # [[5,50],[4,40],... ] 형태의 T와 P 저장 배열
        sch.append([int(a[0]),int(a[1])])
    print(solution(N,sch))