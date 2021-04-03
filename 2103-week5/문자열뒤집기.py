'''
    그리디 03 - 문자열 뒤집기

    다솜이는 0과 1로만 이루어진 문자열 S를 가지고 있습니다. 다솜이는 이 문자열 S에 있는 모든 숫자를 전부 같게하려고 합니다.
    다솜이가 할 수 있는 행동은 S에서 연속된 하나 이상의 숫자를 잡고 모두 뒤집는 것입니다.
    뒤집는 것은 1을 0으로, 0을 1로 바꾸는 것을 의미합니다.
'''

# 연속된 0과 1 시퀀스 중에 개수가 적은 것 return
def solution(S):
    S = list(map(int,S))
    cnt = [0,0]
    S.append(-1)

    prev = S[0]
    for i in range(1,len(S)):
        if prev != S[i]:
            cnt[prev] += 1
        prev = S[i]

    return min(cnt)

if __name__ == '__main__':
    S = input()
    print(solution(S))