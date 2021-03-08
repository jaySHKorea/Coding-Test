'''
    구현 13 치킨배달 - 30m

    크기가 N x N인 도시가 있고, 1 x 1 크기의 칸으로 나누어져 있습니다.

    도시의 각 칸은 빈칸 or 치킨집 or 집 중 하나입니다. 도시의 칸은 (r,c)로 나타냅니다. r와 c는 1부터 나타냅니다.
    0은 빈칸, 1은 집, 2는 치킨집입니다.

    이  도시의 사람들은 치킨을 매우 좋아합니다. 따라서 치킨거리 라는 말은 집과 가장 가까운 치킨집 사이의 거리입니다.
    치킨 커리는 집을 기준으로 정해지며, 각각의 집은 치킨거리를 가지고 있습니다. 도시의 치킨거리는 모든 집의 치킨거리의 합입니다.

    모든 치킨집은 같은 프랜차이즈로, 본사는 일부 치킨집을 폐업시키고 수익을 증가시키려 합니다.
    그리고 오랜 연구 끝에 이 도시에서 가장 수익을 많이 낼 수 있는 치킨집의 개수는 최대 M개라는 것을 알아냈다.

    도시에 있는 치킨집 중에서 최대 M개를 고르고, 나머지 치킨집은 모두 폐업시킵니다. 어떻게 고르면 도시의 치킨 거리가 가장 작아질까요?
'''

import itertools
import sys

def solution(N, M, city):
    answer = int(1e9)
    home = []
    chicken = []

    for i in range(N):
        for j in range(N):
            if city[i][j] == 1:
                home.append((i,j))
            elif city[i][j] == 2:
                chicken.append((i,j))

    # 전체 치킨집 중에 M개만 남기는 조합
    comb = itertools.combinations(chicken,M)

    for c in comb:
        summ = 0
        # 도시의 치킨 거리를 구함
        for h in home:
            summ += distance(h,c)
        if summ < answer :
            answer = summ

    return answer

# 각 집에서 치킨 거리 구하기
def distance(home, comb):
    answer = int(1e9)
    for c in comb: # 남은 치킨 집 중에서 가장 가까운 치킨집 거리 찾기
        d = abs(home[0]-c[0])+abs(home[1]-c[1])
        if d < answer :
            answer = d
    return answer

if __name__ == '__main__':
    N,M = map(int,input().split())
    city = []
    for i in range(N):
        var = list(map(int,sys.stdin.readline().rstrip().split(" ")))
        city.append(var)
    
    print(solution(N,M,city))