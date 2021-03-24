'''
    그래프이론 01 - 여행 계획 30m

    한울이가 사는 나라에는 N개의 여행지가 있고, 각 여행지는 1~N번까지의 번호로 구분된다.
    또한 임의의 두 여행지 사이에는 두 여행지를 연결하는 도로가 존재할 수 있다. 이때 도로는 양방향이다.
    한울이는 하나의 여행 계획을 세운 뒤에 이 여행 계획이 가능한지의 여부를 판단하고자 한다. 

    여행지의 개수와 여행지 간의 연결정보가 주어졌을 때, 한울이의 여행 계획이 가능한지의 여부를 판별하시오.

'''
import sys
from collections import defaultdict

def solution(N,M,mapp,plan):
    answer = 'YES'
    can = defaultdict(set)
    cango = list(set(plan))

    # set 자료구조 만들기
    for i in range(N):
        for j in range(N):
            if mapp[i][j] == 1:
                can[i+1].add(j+1)

    # 가능 통행통로 생성
    for city_num in cango:
        for city in can[city_num]:
            if city in cango:
                can[city].update(can[city_num])

    # 여행 계획 가능 검사
    for i in range(M-1):
        if plan[i+1] not in can[plan[i]]:
            answer = 'False'
            break
    return answer

if __name__ == '__main__':
    N,M = map(int,sys.stdin.readline().rstrip().split(" "))
    mapp = []

    for i in range(N):
        var = list(map(int,sys.stdin.readline().rstrip().split(" ")))
        mapp.append(var)
    plan = list(map(int,sys.stdin.readline().rstrip().split(" ")))
    print(solution(N,M,mapp,plan))