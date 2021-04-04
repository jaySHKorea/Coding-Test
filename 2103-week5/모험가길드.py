'''
    그리디 01 - 모험가길드

    한 마을에 모험가가 N명 있습니다. 모험가 길드에서는 N명의 모험가를 대상으로 공포도를 측정했는데,
    공포도가 높은 모험가는 쉽게 공포를 느껴 위험 상황에서 제대로 대처할 능력이 떨어집니다.
    길드 장인이 모험가 그룹을 안전하게 구성하고자 공포도가 X인 모험가는 반드시 X명 이상으로 구성한 모험가 그룹에 참여해야
    여행을 떠날 수 있습니다.
    이때 최대 몇개의 모험가 그룹을 만들 수 있을까요? N명의 모험가에 대한 정보가 주어졌을 때, 여행을 떠날 수 있는 그룹 수의 최댓값을 구하시오
    
'''
import sys

def solution(N, members):
    answer = 0
    group = 0
    
    members.sort()

    for mem in members:
        group += 1
        if group >= mem:
            answer += 1
            group = 0
    
    return answer

if __name__ == '__main__':
    N = int(input())
    members = list(map(int,sys.stdin.readline().rstrip().split()))
    print(solution(N,members))