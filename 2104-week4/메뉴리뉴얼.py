import itertools
import heapq

# 구현
def solution(orders, course):
    answer = []
    dict = {}
    most = [[] for _ in range(course[-1]+1)]

    for ord in orders:
        order = list(ord)
        order.sort()
        for c in course: # 해당 주문에서 course 개수만큼 가능한 조합
            if len(order) < c:
                continue
            combs = itertools.combinations(order,c)
            for comb in combs: # dict에 조합 기록
                comb = ''.join(comb)
                if comb in dict.keys():
                    dict[comb] += 1
                else:
                    dict[comb] = 1
    
    # 가장 많이 주문된 조합들 찾기
    for key in dict.keys():
        cnum = len(key)
        if most[cnum] and dict[key] >= 2:
            if most[cnum][0][0] == dict[key]: # 같은 최대 횟수
                heapq.heappush(most[cnum],(dict[key],key))
            elif most[cnum][0][0] < dict[key]: # 큰게 나타났을 때
                most[cnum] = []
                heapq.heappush(most[cnum],(dict[key],key))
        elif dict[key] >= 2: # 처음
            heapq.heappush(most[cnum],(dict[key],key))

    for c in course:
        for menu in most[c]:
            answer.append(menu[1])

    answer.sort()
    return answer

print(solution(["XYZ", "XWY", "WXA"], [2,3,4]))
print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"],[2,3,5]))
print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"],[2,3,4]))