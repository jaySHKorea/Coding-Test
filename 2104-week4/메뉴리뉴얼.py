import itertools
import heapq

def solution(orders, course):
    answer = []
    dict = {}
    most = [[] for _ in range(course[-1]+1)]

    for ord in orders:
        order = list(ord)
        order.sort()
        for c in course:
            if len(order) < c:
                continue
            combs = itertools.combinations(order,c)
            for comb in combs:
                comb = ''.join(comb)
                if comb in dict.keys():
                    dict[comb] += 1
                else:
                    dict[comb] = 1
    
    for key in dict.keys():
        cnum = len(key)
        if most[cnum] and dict[key] >= 2:
            if most[cnum][0][0] == dict[key]:
                heapq.heappush(most[cnum],(dict[key],key))
            elif most[cnum][0][0] < dict[key]:
                most[cnum] = []
                heapq.heappush(most[cnum],(dict[key],key))
        elif dict[key] >= 2:
            heapq.heappush(most[cnum],(dict[key],key))

    for c in course:
        for menu in most[c]:
            answer.append(menu[1])

    answer.sort()
    return answer

print(solution(["XYZ", "XWY", "WXA"], [2,3,4]))
print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"],[2,3,5]))
print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"],[2,3,4]))