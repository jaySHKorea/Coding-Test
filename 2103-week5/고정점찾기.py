'''
    이진탐색 02 - 고정점 찾기
    
    고정점이란, 수열의 원소 중에서 그 값이 인덱스와 동일한 원소를 의미합니다.
    하나의 수열이 N개의 서로 다른 원소를 포함하고 있고, 모든 원소가 오름차순으로 정렬되어 있습니다.
    이때 이 수열에서 고정점이 있다면, 고정점을 출력하는 프로그램을 작성하세요. 고정점은 최대 1개입니다. 만약 고정점이 없다면 -1을 출력합니다.
    단, 이 문제는 시간 복잡도 O(logN)으로 설계하지 않으면 시간 초과 판정을 받습니다.
'''
import sys

def solution(start,end,array):
    while start <= end:
        mid = (start+end) // 2
        if array[mid] == mid:
            return mid
        if array[mid] >= len(array)-1:
            end = mid-1
        else:
            start = mid + 1
    return -1

if __name__ == '__main__':
    N = int(input())
    array = list(map(int,sys.stdin.readline().rstrip().split(" ")))
    print(solution(0,N-1,array))