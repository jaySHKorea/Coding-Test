'''
    이진탐색 01 - 정렬된 배열에서 특정 수의 개수 구하기

    N개의 원소를 포함하고 있는 수열이 오름차순으로 정렬되어 있습니다. 이때 이 수열에서 x가 등장하는 횟수를 계산하세요.
    단, 이 문제는 시간 복잡도 O(logN)으로 알고리즘을 설계하지 않으면 시간 초과 판정을 받습니다. 
'''

import sys

def solution(start, end, target, array):
    if target not in array:
        return -1

    return binary(start,end,target,array,0)-binary(start,end,target,array,1)

# 가장 작은 점
def binary(start,end,target,array,sign):
    while start <= end:
        mid = (start+end) // 2
        if array[mid] == target:
            if sign == 0:
                start = mid+1
            elif sign == 1:
                end = mid-1
        elif array[mid] < target:
            start = mid+1
        else:
            end = mid-1
    return start

if __name__ == '__main__':
    N,x = map(int,sys.stdin.readline().rstrip().split(" "))
    array = list(map(int,sys.stdin.readline().rstrip().split(" ")))
    print(solution(0,N-1,x,array))