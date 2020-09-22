# 프로그래머스 징검다리 : 이분탐색
'''
출발지점부터 distance만큼 떨어진 곳에 도착지점이 있습니다.
그리고 그사이에는 바위들이 놓여있습니다. 바위 중 몇 개를 제거하려고 합니다.
예를 들어, 도착지점이 25만큼 떨어져 있고, 바위가 [2, 14, 11, 21, 17] 지점에 놓여있을 때
바위 2개를 제거하면 출발지점, 도착지점, 바위 간의 거리가 아래와 같습니다.
'''

# 제한사항
'''
도착지점까지의 거리 distance는 1 이상 1,000,000,000 이하입니다.
바위는 1개 이상 50,000개 이하가 있습니다.
n 은 1 이상 바위의 개수 이하입니다.
'''

# 0 2 11 14 17 21
# 2 9 3 3 4 

# 첫번째 아이디어
'''
1. 돌 사이의 거리 값을 key로 배열을 정렬
2. 가장 작은 값을 pop하고
3. 다시 돌 위치 값을 key로 배열을 정렬
4. pop한 값의 좌우 거리에 대해서 더 작은 값인 돌의 위치를 택해서 더한 후 append

위를 n번 반복한 후에 돌 사이의 거리 값을 key로 배열을 정렬
가장 작은 0 인덱스 값 return

=> sort를 너무 많이함
'''

# 더 좋은 정답
'''
1. 정렬은 초기 한번
2. 이분 탐색 값은 돌 사이의 거리 -> (0과 distance)/2를 mid로 시작
3. mid와 left,right를 움직인다 -> 기준은 지운 돌의 개수가 n보다 큰지 작은지에 따라
4. 돌을 지우는 반복문은 prev,mid에 따라 현재 돌과 이전 돌 사이의 거리가 이분 탐색 기준 값보다
    작냐 크냐에 따라 돌을 지우거나 , 지우지 않고 min값에 담아 prev를 다음돌로 이동한다

mid = (left+right) == 10일때
prev = 0 r = 2 -> mid 보다 거리가 작으므로 2 돌을 지운다
prev = 0 r = 11 -> mid 보다 거리가 크므로  mins를 r-prev로 바꾼다, prev는 11이 됨
prev = 11 r = 14 -> mid보다 거리가 작으므로 14 돌을 지운다
prev = 11 r = 17 -> mid보다 거리가 작으므로 17 돌을 지운다
prev = 11 r = 21 -> mid랑 거리가 같으므로 mins를 r-prev로 바꾼다. prev는 21이 됨
prev = 21 r = 25 -> mid보다 거리가 작으므로 25 돌을 지운다
'''

'''
def solution1(distance, rocks, n):
    rocks = sorted(rocks)
    rocks.insert(0,0)
    rocks.append(25)
    rock_dist = []
    for i,r in enumerate(rocks):
        if i == 0: continue
        rock_dist.append([rocks[i-1],r,r-rocks[i-1]])

    while ( n != 0 ):
        rock_dist = sorted(rock_dist,key=lambda x : x[2])
        mini = rock_dist.pop(0)
        rock_dist = sorted(rock_dist,key=lambda x : x[0])
        if mini[0] == 0 :
            idx,loc = b_search(rock_dist,mini[1])
            tmp = rock_dist.pop(idx)
            rock_dist.append([0,tmp[loc],mini[2]+tmp[2]])
        elif mini[1] == distance :
            idx,loc = b_search(rock_dist,mini[0])
            tmp = rock_dist.pop(idx)
            rock_dist.append([tmp[loc],distance,mini[2]+tmp[2]])
        else :
            idx1,loc1 = b_search(rock_dist,mini[0])
            idx2,loc2 = b_search(rock_dist,mini[1])

            if ( rock_dist[idx1][2] < rock_dist[idx2][2]):
                tmp = rock_dist.pop(idx1)
                rock_dist.append([tmp[loc1],mini[1],tmp[2]+mini[2]])
            else:
                tmp = rock_dist.pop(idx2)
                rock_dist.append([mini[0],tmp[loc2],tmp[2]+mini[2]])
        n -= 1

    rock_dist = sorted(rock_dist,key=lambda x : x[2])
    return rock_dist[0][2]

def b_search(l,s_num):
    left = 0
    right = len(l)-1
    mid = int(len(l)/2)

    while ( True ):
        if ( l[mid][0] == s_num or l[mid][1] == s_num):break
        if ( s_num < l[mid][0]):
            right = mid
        else:
            left = mid
        mid = int((left+right)/2)
    
    if ( l[mid][0] == s_num):
        return mid,1
    else:
        return mid,0
'''

import math

def solution2(distance, rocks, n):
    rocks.sort()
    rocks.append(distance)
    left, right = 0, distance
    answer = 0

    while left <= right:
        prev = 0
        mins = math.inf
        removed = 0

        # 바위 사이의 최소 거리
        mid = int((left+right)/2)
        # 제거할 돌 찾기
        for r in rocks:
            # 최소거리보다 작은 간격의 돌을 찾음
            # r 위치의 돌을 지움 -> prev와 다음 r 위치의 돌을 비교
            if r-prev < mid:
                removed += 1
            else: # 가장 큰 최소 거리 발견 mins 바꾸고, 다음돌로 뛰어넘음 prev=r
                mins = min(mins,r-prev)
                prev = r

        # 제거한 돌 개수가 기준보다 많다 : 최소거리를 줄인다
        if removed > n:
            right = mid-1
        # 제거한 돌 개수가 기준보다 적거나 같다 : answer를 바꾸고 최소거리를 늘린다
        else:
            answer = mins
            left = mid+1

    return answer
print(solution2(25,[2,14,11,21,17],2))