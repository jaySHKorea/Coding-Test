'''
    입력된 정수 N에 대해 00시 00분 00초부터 N시 59분 59초까지의 모든 시각 중에서 3이 하나라도 포함되는 모든 경우의 수를 구하는 프로그램을 작성하시오 
    원래는 3중 완전탐색
'''

def countTime(N):
    allCase = (N+1)*6*10*6*10

    # 3이 하나도 없는 경우
    if ( N >= 3 ):
        ex = N*5*9*5*9
    else:
        ex = (N+1)*5*9*5*9
    
    return allCase-ex

if __name__ == '__main__':
    N = int(input())
    print(countTime(N))
