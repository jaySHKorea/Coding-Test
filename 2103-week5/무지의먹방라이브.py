'''
    그리디 06 - 무지의 먹방 라이브

    회전판에 먹어야할 N개의 음식이 있고, 음식은 1부터 N까지의 번호가 있으며, 각 음식을 섭취하는데
    일정 시간이 소요됩니다. 무지는 다음과 같은 방법으로 음식을 섭취합니다.

    1. 무지는 1번음식부터 먹기 시작하며, 회전판은 번호가 증가하는 순서대로 음식을 무지 앞으로 가져다 놓습니다.
    2. 마지막 번호의 음식을 섭취한 후에는 회전판에 의해 다시 1번 음식이 무지 앞으로 옵니다.
    3. 무지는 음식 하나르 1초 동안 섭취한 후 남은 음식은 그대로 두고, 다음 음식을 섭취합니다.
    다음 음식이란, 아직 남은 음식 중 다음으로 섭취해야할 가장 가까운 번호의 음식을 말합니다.
    4. 회전판이 다음 음식을 무지 앞으로 가져오는데 걸리는 시간은 없습니다.

    무지가 먹방을 시작한 지 K초 후에 네트워크 장애로 방송이 잠시 중단되었습니다. 무지는 네트워크 정상화 후, 몇번 음식부터
    섭취해야하는지 알고자 합니다. 
'''

def solution(food_times, k):
    answer = -1
    N = len(food_times)
    i = -1

    # 먹기 시작
    while k > 0:
        i = (i+1)%3
        if food_times[i] != 0:
            food_times[i] -= 1
            k -= 1
        else:
            continue
    
    for j in range(N):
        i = (i+1)%3
        if food_times[i] != 0:
            answer = i+1
            break
    
    return answer

from collections import deque
def solution1(food_times, k):
    answer = -1
    round = deque()

    for i in range(len(food_times)):
        round.append((i+1,food_times[i]))

    # 먹기 시작
    while k > 0:
        num, amount = round.popleft()
        amount -= 1
        if amount != 0:
            round.append((num,amount))
        k -= 1

    if round:
        answer = round[0][0]
    return answer

import heapq
def solution2(food_times, k):
    answer = -1
    round = []
    N = len(food_times)

    if sum(food_times) <= k:
        return answer

    for i in range(len(food_times)):
        heapq.heappush(round,(food_times[i],i))

    prev = 0
    # 먹기 시작
    while True:
        cnt = len(round)
        amount,num = heapq.heappop(round)
        k -= (amount-prev)*cnt
        if (amount-prev)*len(round) > k:
            break
        prev = amount
    
    if round:
        round = sorted(round,key=lambda x:x[1])
        answer = round[k%len(round)][1]+1
    return answer

def solution3(food_times, k):
    low, high = 0,sum(food_times)
    n, cutting, idx = len(food_times),0,0
    while low <= high:
        mid = (low+high)//2
        v = n*mid
        for f in food_times:
            tmp = f-mid
            if tmp < 0:
                v += tmp
        if v <= k:
            cutting,idx = mid,v
            low = mid+1
        else:
            high = mid-1
    food_times = [f-cutting for f in food_times]

    for i in range(n):
        if food_times[i] > 0 and idx==k:
            return i+1
        else:
            if food_times[i] > 0:
                idx += 1
    return -1

print(solution3([3, 1, 2],5))
print(solution3([4,2,3,6,7,1,5,8],27))