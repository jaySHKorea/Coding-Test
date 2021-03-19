'''
    DP 02 정수 삼각형 - 백준 1932

    정수 삼각형이 있을때, 맨 위에서 부터 아래로 내려올 때, 이제까지 선택된 수의 합이 최대가 되는 경로를 구하는 프로그램을 작성하시오
    수는 대각선 왼쪽또는 오른쪽에 잇는 것을 선택할 수 있습니다.
    삼각형의 크기는 1이상 500이하이고 정수입니다.

    점화식
        new_tri[i+1][j] = max(new_tri[i][j]+tri[i+1][j],new_tri[i+1][j])
        new_tri[i+1][j+1] = max(new_tri[i][j]+tri[i+1][j+1],new_tri[i+1][j+1])
'''

import sys
from copy import deepcopy

def solution(n,tri):
    new_tri = deepcopy(tri)
    for i in range(0,n-1):
        for j in range(len(tri[i])):
            new_tri[i+1][j] = max(new_tri[i][j]+tri[i+1][j],new_tri[i+1][j])
            new_tri[i+1][j+1] = max(new_tri[i][j]+tri[i+1][j+1],new_tri[i+1][j+1])

    return max(new_tri[n-1])

if __name__ == '__main__':
    n = int(input())
    tri = []

    for i in range(n):
        var = list(map(int,sys.stdin.readline().rstrip().split(" ")))
        tri.append(var)
    
    print(solution(n, tri))