'''
    dfs/bfs 05 백준 14888

    N개의 수로 이루어진 수열이 주어집니다. 수와 수 사이에 끼워 넣을 수 있는 N-1개의 연산자가 주어집니다.
    연산자는 +,-,*,/ 로 이루어져있습니다.
    이때 수와 수 사이에 연산자를 하나씩 넣어서, 수식을 하나 만들 수 있는데 이때 주어진 수의 순서를 바꾸면 안됩니다.

    식의 계산은 연산자 우선순위를 무시하고 앞에서부터 진행해야 합니다. 또, 나눗셈은 정수 나눗셈으로 몫만 취합니다.
    음수를 양수로 나눌때는 음수를 양수로 바꾼 뒤 몫을 취하고 음수로 바꿉니다.

    만들 수 있는 식의 결과가 최대인 것과 최소인 것을 구하는 프로그램을 작성하세요.
'''
import sys
import itertools

def solution(N,num,sign):
    maxx = 0 
    minn = 0
    s = []
    for i in range(sign[0]):
        s.append('+')
    for i in range(sign[1]):
        s.append('-')
    for i in range(sign[2]):
        s.append('*')
    for i in range(sign[3]):
        s.append('/')
    
    comb = itertools.permutations(s,N-1)
    
    for i,c in enumerate(comb):
        answer = calculate(num,c)
        if i == 0:
            maxx = answer
            minn = answer
        else:
            maxx = max(answer,maxx)
            minn = min(answer,minn)

    print(maxx)
    print(minn)

def calculate(num,sign):
    start = num[0]
    for i in range(len(sign)):
        a,b = num[i+1],sign[i]
        if b == '+':
            start += a
        elif b == '-':
            start -= a
        elif b == '*':
            start *= a
        elif b == '/':
            if a < 0 :
                start = -int(abs(start)/a)
            else:
                start = int(start/a)
    return start


if __name__ == '__main__':
    N = int(input())
    num = list(map(int,sys.stdin.readline().rstrip().split(" "))) #도시개수, 도로개수, 거리정보, 출발도시번호 X
    sign = list(map(int,sys.stdin.readline().rstrip().split(" ")))
    solution(N,num,sign)