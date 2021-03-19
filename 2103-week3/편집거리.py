'''
    DP 06 편집 거리 - 최소 편집거리 알고리즘(Minimum Edit Distance)

    두 개의 문자열 A와 B가 주어졌을 때, 문자열 A를 편집하여 문자열 B로 만들고자 한다.
    문자열 A를 편집할 때는 다음의 세 연산 중에서 한번에 하나씩 선택하여 이용할 수 있다.

    1. 삽입
    2. 삭제
    3. 교체

    이때 편집거리란 문자열 A를 편집하여 문자열 B로 만들기 위해 사용한 연산의 수를 의미한다.
    A를 B로 만들기 위한 최소 편집거리를 계산하는 프로그램을 작성하시오.
'''

import sys

def solution(org, tobe):
    w,h = len(org),len(tobe)
    mat = [[0 for _ in range(w+1)] for _ in range(h+1)]

    # 배열초기화
    for i in range(w+1):
        mat[0][i] = i
    for i in range(h+1):
        mat[i][0] = i

    # matrix 계산
    for i in range(1,h+1):
        for j in range(1,w+1):
            if org[j-1] == tobe[i-1]:
                mat[i][j] = mat[i-1][j-1]
            else:
                mat[i][j] = min(mat[i][j-1],mat[i-1][j-1],mat[i-1][j])+1 # 단어추가/단어편집/단어삭제

    return mat[h][w]

if __name__ == '__main__':
    org = list(sys.stdin.readline().rstrip())
    tobe = list(sys.stdin.readline().rstrip())

    print(solution(org,tobe))