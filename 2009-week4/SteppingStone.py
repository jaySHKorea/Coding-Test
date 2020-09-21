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

def solution(distance, rocks, n):
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



print(solution(25,[2,14,11,21,17],2))
