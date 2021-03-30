'''
    이진검색 03 - 공유기 설치

    도현이의 집 N개가 수직선 위에 있습니다. 각각의 집의 좌표는 x1,x2,...xn이고, 집 여러개가 같은 좌표를 가지지 않습니다.
    도현이는 언제 어ㄷ서나 와이파리를 사용하기 위해 집에 공유기 C개를 설치합니다. 
    최대한 많은 곳에서 와이파이를 사용하려고 하기 때문에, 한 집에는 공유기를 하나만 설치할 수 있고,
    가장 인접한 두 공유기 사이의 거리를 가능한 크게하여 설치하려고 합니다. 
    C개의 공유기를 N개의 집에 적당히 설치해서, 인접한 두공유기 사이의 거리를 최대로 하는 프로그램을 작성하세요.
'''

import sys

def solution(N,C,house):
    answer = 0
    house.sort()
    start = 1
    end = house[N-1]-house[0]

    while start <= end:
        mid = (start+end) // 2
        if check(mid,N,C,house):
            answer = max(answer,mid)
            start = mid+1
        else:
            end = mid-1
    return answer

def check(dist,N,C,house):
    cnt = 1
    prev = house[0]

    for i in range(1,N):
        if house[i]-prev >= dist:
            cnt += 1
            prev= house[i]
    if cnt >= C:
        return True
    return False

if __name__ == '__main__':
    N,C = map(int,sys.stdin.readline().rstrip().split(" "))
    house = []
    for i in range(N):
        house.append(int(input()))
    print(solution(N,C,house))