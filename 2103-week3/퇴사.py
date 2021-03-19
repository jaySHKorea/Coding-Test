'''
    DP 03 퇴사 백준 14501

    상담원으로 일하고 있는 백준이는 퇴사를 하려고 한다. 오늘부터 N+1일째 되는 날 퇴사를 하기 위해서 남은 N일동안 최대한 많은 상담을 하려고 한다.
    백준이는 비서에게 최대한 많은 상담을 잡으라고 부탁을 했고, 비서는 하루에 하나씩 서로 다른 사람의 상담을 잡아 놓았습니다.
    각각의 상담은 상담을 완료하는데 거리는 기간 Ti와 상담을 했을 때 받을 수 있는 금액 Pi로 이루어져 있습니다.

    상담을 적절히 했을때, 백준이가 얻을 수 있는 최대 수익을 구하시오.

    # 각 i에 대한 dp를 만들때 이전의 j들을 살피고, i로 합쳐질 수 있는 값을 계산
'''

import sys

def solution(n,Ti,Pi):
    answer = 0 
    c = [0 for _ in range(n+1)]

    for i in range(0,n+1):
        for j in range(0,i):
            c[i] = max(c[i],c[j])
            if j + Ti[j] == i:
                c[i] = max(c[i],c[j]+Pi[j])
        answer = max(answer,c[i])
    return answer

if __name__ == '__main__':
    n = int(input())
    Ti = []
    Pi = []

    for i in range(n):
        var = list(map(int,sys.stdin.readline().rstrip().split(" ")))
        Ti.append(var[0])
        Pi.append(var[1])
    
    print(solution(n,Ti,Pi))