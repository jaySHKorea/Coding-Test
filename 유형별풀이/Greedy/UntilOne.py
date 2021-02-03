'''
    어떤 수 N이 1이 될 때까지 다음의 두 과정 중 하나를 반복적으로 수행한다.
    단 두번째 연산은 N%K==0이어야 가능하다

    2<= N <= 100000, 2 <= K <= 100000, 공백으로 구분된 자연수, N >= K
'''

import sys

def divide(N,K):
    answer = 0

    while ( N != 1 ):
        if ( N%K == 0 ) : N = N/K
        else : N -= 1
        answer += 1
    
    return answer


if __name__ == '__main__':
    N,K = map(int,sys.stdin.readline().rstrip().split(" "))
    print(divide(N,K))