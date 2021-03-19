'''
    DP 01 금광

    n x m 크기의 금광이 있다. 금광은 1x1로 나누어져있고, 각 칸은 특정한 크기의 금이 들어있다.
    채굴자는 첫 번째 열부터 출발하여 금을 캐기 시작한다.
    맨 처음에는 첫번째 열의 어느 행에서든 출발할 수 있다. 이후 m번에 걸쳐서 매번 오른쪽 위, 오른쪽 , 오른쪽 아래 3가지 중 하나의 위치로 이동해야한다.
    결과적으로 채굴자가 얻을 수 있는 금의 최대 크기를 출력하시오.

    점화식 : cal[j][i] = max(a+cal[j-1][i-1],a+cal[j][i-1],a+cal[j+1][i-1])
'''
import sys

def solution(T,gold):
    for n,m,arr in gold:
        cal = [arr[i*m:i*m+4] for i in range(n)]
        for i in range(1,m):
            for j in range(0,n):
                a = cal[j][i]
                if j-1 > 0 and j+1 < n:
                    cal[j][i] = max(a+cal[j-1][i-1],a+cal[j][i-1],a+cal[j+1][i-1])
                elif j-1 > 0:
                    cal[j][i] = max(a+cal[j-1][i-1],a+cal[j][i-1])
                else:
                    cal[j][i] = max(a+cal[j][i-1],a+cal[j+1][i-1])  
        print(find_max(n,m,cal))

def find_max(n,m,cal):
    answer = 0
    for i in range(n):
        answer = max(answer,cal[i][m-1])
    return answer

if __name__ == '__main__':
    T = int(input())
    gold = []

    for i in range(T):
        n,m = map(int,sys.stdin.readline().rstrip().split(" "))
        var = list(map(int,sys.stdin.readline().rstrip().split(" ")))
        gold.append((n,m,var))
    
    solution(T,gold)