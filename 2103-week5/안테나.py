'''
    정렬 02 - 안테나

    일직선상의 마을에 여러 채의 집이 위치해있다. 이 중에서 특정 위치의 집에 특별히 한개의 안테나를 설치한다.
    효율성을 위해 안테나로부터 모든 집까지의 거리의 총합이 최소가 되도록 설치한다. 이때, 안테나는 집이 위치한 곳에만 설치 가능하고,
    논리적으로 동일한 위치에 여러개의 집이 존재할 수 있습니다.
    집들의 위치 값이 주어질 때, 안테나를 설치할 위치를 고르는 프로그램을 작성하세요.
'''
import sys

def solution(N,house):
    house.sort()
    half = int((N-1)/2)
    return house[half]

if __name__ == '__main__':
    N = int(input())
    house = list(map(int,sys.stdin.readline().rstrip().split(" ")))
    print(solution(N,house))