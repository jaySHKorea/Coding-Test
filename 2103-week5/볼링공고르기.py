'''
    그리디 05 - 볼링공 고르기

    A,B 두 사람이 볼링을 치고 있다. 두 사람은 서로 무게가 다른 볼링공을 고르려고 한다.
    볼링공은 총 N개가 있고 각 볼링공마다 무게가 적혀있고, 번호는 1번부터 부여된다.
    또한 같은 무게의 공이 여러 개 있을 수 있지만 서로 다른 공이다.
    볼링공의 무게는 1부터 M까지 자연수의 형태로 존재한다.
'''
import sys
import math
from itertools import combinations

def solution(N,M,balls):
    redup = [0 for _ in range(M+1)]
    redup_cnt = 0

    for b in balls:
        redup[b] += 1

    for r in redup:
        if r >= 2:
            redup_cnt += int(math.factorial(r)/math.factorial(r-2)/2)
    
    # 전체 조합수 - 중복인 경우
    return int(math.factorial(N)/math.factorial(N-2)/2)-redup_cnt

if __name__ == '__main__':
    N,M = map(int,sys.stdin.readline().rstrip().split())
    balls = list(map(int,sys.stdin.readline().rstrip().split()))
    print(solution(N,M,balls))