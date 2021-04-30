''' 이진 탐색 2회차 '''
import math

def solution(distance,rocks,n):
    answer = 0
    rocks.sort()
    rocks.append(distance)
    left, right = 0, distance

    while left <= right:
        prev = 0
        mins = math.inf
        removed = 0

        mid = int((left+right)/2)
        for r in rocks:
            if r-prev < mid:
                removed += 1
            else: 
                mins = min(mins,r-prev)
                prev = r

        if removed > n:
            right = mid-1
        else:
            answer = max(answer,mins)
            left = mid+1
    return answer