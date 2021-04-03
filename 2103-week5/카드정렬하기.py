'''
    정렬 04 - 카드 정렬하기

    정렬된 두 묶음의 숫자 카드가 있을 때, 각 묶음의 카드의 수를 A,B라 하면 보통 두 묶음을 합쳐서
    하나로 만드는 데에는 A+B번의 비교를 해야합니다.
    매우 많은 숫자 카드 묶음이 책상 위에 놓여 있습니다. 이들을 두 묶음씩 골라 서로 합쳐나간다면, 고르는 순서에 따라
    비교횟수가 매우 달라집니다.

    N개의 숫자 카드 묶음의 각각의 크기가 주어질 때 최소한 몇번의 비교가 필요한지 구하시오.
'''
import heapq

def solution(N,cards):
    answer = 0

    while len(cards) > 1:
        a,b = heapq.heappop(cards),heapq.heappop(cards)
        answer += a+b
        heapq.heappush(cards,a+b)
    
    return answer

if __name__ == '__main__':
    N = int(input())
    cards = []
    for i in range(N):
        heapq.heappush(cards,int(input()))
    print(solution(N,cards))