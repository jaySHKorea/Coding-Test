'''
    동빈이네 떡집의 떡볶이 떡은 길이가 일정하지 않다. 대신에 한 봉지 안에 들어가는 떡의 총 길이는
    절단기로 잘라서 맞춰준다.
    절단기에 높이 H를 지정하면 줄지어진 떡을 한번에 절단한다. 높이 H 보다 긴 떡은 H 위의 부분이 잘리고,
    낮은 떡은 잘리지 않는다.

    손님이 왔을 때 요청한 총 길이가 M일때 적어도 M만큼의 떡을 얻기 위해 절단기에 설정할 수 있는 H의 최댓값을 구하시오.
    절단기 H의 가능한 길이 == 0 ~ 제일 긴 떡의 길이
    -> mid가 H라고 할때 total(잘린 떡의 총합, sum(떡길이-mid))을 계산하여
    => 잘린 떡의 총합이 모자라면 더 H가 짧아지게 end = mid-1
    => 잘린 떡의 총합이 많거나 
'''
import sys

def binary_search2(array, target, start, end):
    answer = 0
    while start <= end:
        total = 0
        # 절단기 길이
        mid = (start+end) // 2
        # 잘린 떡 양 계산
        for i in array:
            if ( i > mid ):
                total += i-mid
        # 떡의 양이 부족할 때( 더 잘라야함 == 절단기 길이가 짧아져야함 )
        if total < target:
            end = mid - 1
        # 떡의 양이 만족했거나 더 많을 때 
        else:
            if ( answer < mid ): #mid는 최대값이어야함
                answer = mid
            start = mid + 1
    return answer

if __name__ == '__main__':
    N,M = map(int,input().split())
    tteok = list(map(int,sys.stdin.readline().rstrip().split()))
    print(binary_search2(tteok,M,0,max(tteok)))
