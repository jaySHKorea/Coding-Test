'''
    이진탐색 - 입국심사

    처음에 모든 심사대는 비어있고, 한 심사대에서는 동시에 한 명만 심사가능
    가장 앞에 서있는 사람은 비어 있는 심사대로 가거나, 더 빨리 끝나는 심사대가 있으면 기다렸다가 그곳으로 갑니다.
    모든 사람이 심사를 받는데 걸리는 시간을 최소로 하고 싶습니다.
'''

# 처리가 끝나는 시간은 times(처리시간)의 특정 수의 배수이다.

def solution(n, times):
    answer = -1
    times.sort()
    start = 0
    end = times[-1]*n

    '''# 오버헤드
    for time in times:
        array += [ time*i for i in range(1,n+1)]
    '''

    while start <= end:
        mid = (start+end)//2
        cnt = 0
        for time in times:
            cnt += mid//time
        if cnt >= n: # 처리한 사람 수가 동일하거나 더 많을 때도 갱신
            if answer == -1:
                answer = mid
            else:
                answer = min(answer,mid)
            end = mid-1
        else:
            start = mid+1

    return answer

print(solution(6, [7, 10]))