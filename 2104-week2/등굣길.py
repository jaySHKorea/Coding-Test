'''
    DP - 등굣길

    계속되는 폭우로 일부 지역이 물에 잠겼습니다. 물에 잠기지 않은 지역을 통해 학교를 가려고 합니다. 집에서 학교까지 가는 길은 m x n 크기의 격자모양으로 나타낼 수 있습니다.
    격자의 크기 m, n과 물이 잠긴 지역의 좌표를 담은 2차원 배열 puddles이 매개변수로 주어집니다.
    오른쪽과 아래쪽으로만 움직여 집에서 학교까지 갈 수 있는 최단경로의 개수를 1,000,000,007로 나눈 나머지를 return 하도록 solution 함수를 작성해주세요.
'''

# 좌표 표시 (x,y) (y,x)인지 유의
def solution(m, n, puddles):
    answer = 0
    array = [[0 for _ in range(m+2)] for _ in range(n+2)]

    for i in range(1,n+1):
        for j in range(1,m+1):
            if i == 1 and j == 1:
                array[i][j] = 1
            elif [j,i] not in puddles:
                array[i][j] = array[i][j-1]+array[i-1][j]
    answer = array[n][m]
    return answer%1000000007

print(solution(4,3,[[2, 2]]))