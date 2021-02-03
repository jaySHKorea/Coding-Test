'''
    N(행) x M(열) 형태로 놓여있는 카드
    카드를 고르는 규칙은 특정 행을 선택하고, 그 중에 가장 작은 수의 카드를 가진다.
    가장 높은 수의 카드를 얻자.
'''

import sys

def select_card(N,cards):
    answer = -1
    for i in range(N):
        min_value = min(cards[i])
        answer = max(answer, min_value)
    
    return answer


if __name__ == '__main__':
    cards = []
    N,M = map(int,sys.stdin.readline().rstrip().split(" "))

    for i in range(0,N):
        cards.append(list(map(int,sys.stdin.readline().rstrip().split())))
    print(select_card(N,cards))