'''
    DP 05

    못생긴 수란 오직 2,3,5만을 소인수로 가지는 수를 의미합니다. 다시 말해, 오직 2,3,5를 약수로 가지는 합성수를 의미합니다.
    1은 못생긴 수라고 가정합니다. 이때, n번째 못생긴 수를 찾는 프로그램을 작성하세요.
'''

import heapq

def solution(n):
    cnt = 1
    heap = []
    pop = []
    heapq.heappush(heap,1)

    while True:
        num = heapq.heappop(heap)
        if num not in pop:
            pop.append(num)
        else:
            continue
        if cnt == n:
            break
        heapq.heappush(heap,num*2)
        heapq.heappush(heap,num*3)
        heapq.heappush(heap,num*5)
        cnt += 1
    return num


if __name__ == '__main__':
    n = int(input())
    print(solution(n))