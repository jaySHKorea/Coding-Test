'''
    동빈이네 전자 매장에는 부품이 N개 있다. 각 부품은 정수 형태의 고유한 번호가 있는데,
    손님이 M개 종류의 부품을 대량으로 구매하겠다며 당일날 견적서를 요청했다. 이때 M개의 부품이 존재하는지 안하는지
    확인하는 프로그램을 작성해보자.
'''
import sys

def binary_search2(array, target, start, end):
    while start <= end:
        mid = (start+end) // 2

        if array[mid] == target:
            return 'yes'
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return 'no'

# 이진 탐색 ver.
if __name__ == '__main__':
    N = int(input())
    all_list = list(map(int,sys.stdin.readline().rstrip().split()))
    M = int(input())
    req_list = list(map(int,sys.stdin.readline().rstrip().split()))

    all_list.sort()
    for req in req_list:
        print(binary_search2(all_list,req,0,N-1),end=' ')

# 계수정렬(count sort) ver.
if __name__ == '__main__':
    N = int(input())
    array = [0] * 1000001
    for i in sys.stdin.readline().rstrip().split():
        array[int(i)] = 1

    M = int(input())
    req_list = list(map(int,sys.stdin.readline().rstrip().split()))

    for req in req_list:
        if array[req] == 1:
            print('yes',end='')
        else:
            print('no', end=' ')

# 집합 자료 in 사용
if __name__ == '__main__':
    N = int(input())
    all_list = list(map(int,sys.stdin.readline().rstrip().split()))
    M = int(input())
    req_list = list(map(int,sys.stdin.readline().rstrip().split()))

    for req in req_list:
        if req in all_list:
            print('yes',end='')
        else:
            print('no', end=' ')
