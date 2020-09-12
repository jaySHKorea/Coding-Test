# 프로그래머스 입국심사 -이분탐색
'''
n명이 입국심사를 위해 줄을 서서 기다리고 있습니다.
각 입국심사대에 있는 심사관마다 심사하는데 걸리는 시간은 다릅니다.
처음에 모든 심사대는 비어있습니다.
한 심사대에서는 동시에 한 명만 심사를 할 수 있습니다.
가장 앞에 서 있는 사람은 비어 있는 심사대로 가서 심사를 받을 수 있습니다.
하지만 더 빨리 끝나는 심사대가 있으면 기다렸다가 그곳으로 가서 심사를 받을 수도 있습니다.
모든 사람이 심사를 받는데 걸리는 시간을 최소로 하고 싶습니다.
입국심사를 기다리는 사람 수 n, 각 심사관이 한 명을 심사하는데 걸리는 시간이 담긴 배열 times가 매개변수로 주어질 때,
모든 사람이 심사를 받는데 걸리는 시간의 최솟값을 return 하도록 solution 함수를 작성해주세요.
'''
# 제한사항
'''
입국심사를 기다리는 사람은 1명 이상 1,000,000,000명 이하입니다.
각 심사관이 한 명을 심사하는데 걸리는 시간은 1분 이상 1,000,000,000분 이하입니다.
심사관은 1명 이상 100,000명 이하입니다.
'''
def search(left, right, times, n):
    cnt=0
    answer = -1 # 양수아니고 무조건 음수!!!
    while (left <= right):
        mid = int((left+right)/2) # 시간을 반으로 줄였을때  
        cnt = 0
        for time in times:
            cnt += int(mid/time) # 모든 심사원들이 처리할 수 있는 사람 수

        if ( cnt >= n ): # 처리해야할 사람보다 더 많이 처리 했다 : 시간이 더 적게 걸릴 수 있다
            if ( answer == -1):
                answer = mid
            else:
                answer = min(answer,mid) # answer 바꿈
            right = mid-1 # 더 적어질 수 있으므로 right = mid-1
        else:
            left = mid+1 # 처리해야할 사람보다 더 적게 처리했다 : 더 많이 시간이 필요하다 -> left = mid+1

    return answer

def solution(n, times):
    times=sorted(times)
    left = 0
    right = times[-1]*n
    answer = search(left, right, times, n)
    return answer

print(solution(6, [7, 10])) #return : 28
#print(solution(10,[3,8,3,6,9,2,4])) #return : 8