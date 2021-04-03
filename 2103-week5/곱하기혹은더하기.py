'''
    그리디 02 - 곱하기 혹은 더하기

    각 자리가 숫자0~9까지로만 이루어진 문자열 s가 주어졌을 때, 왼->오 방향으로 하나씩 모든 숫자를 확인하며
    숫자 사이에 x 혹은 + 연산자를 넣어 결과적으로 만들어질 수 있는 가장 큰수를
    구하는 프로그램을 작성하세요.
    모든 연산은 일반 계산방식과 다르게 왼->오로 이루어집니다.
'''

def solution(S):
    S = list(map(int,S))
    answer = S[0]
    for i in range(1,len(S)):
        answer = max(answer*S[i],answer+S[i])

    return answer

if __name__ == '__main__':
    S = input()
    print(solution(S))