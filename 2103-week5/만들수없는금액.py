'''
    그리디 04 - 만들 수 없는 금액

    동네 편의점의 주인은 N개의 동전을 가지고 있습니다. 이때 N개의 동전을 이용하여 만들수 없는 양의 정수 금액 중 최솟값을 구하는 프로그램을 작성하시오.
    예를 들어, N=5이고, 각 동전이 각각 3원, 2원,1원,1원,9원 동전이라고 가정합니다.
    이때 만들 수 없는 양의 정수 금액 중 최솟값은 8원입니다.
'''
import sys
from itertools import combinations

def solution(N,coins):
    answer = 0
    possible = [0 for i in range(sum(coins)+2)]
    
    for i in range(1,N+1):
        comb = combinations(coins,i)
        for c in comb:
            possible[sum(c)] = 1

    for i in range(1,len(possible)):
        if possible[i] == 0:
            return i

if __name__ == '__main__':
    N = int(input())
    coins = list(map(int,sys.stdin.readline().rstrip().split()))
    print(solution(N,coins))