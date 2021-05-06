# sol1 : 이진탐색+슬라이딩윈도우
# sol2 : 투포인터

from collections import defaultdict

def solution(gems):
    gem_num = len(set(gems))

    if gem_num == 1:
        return [1,1]
    
    N = len(gems)
    start,end = 0,1
    gemdict = defaultdict(int)
    gemdict[gems[start]] += 1
    gemdict[gems[end]] += 1
    answer = [start,end]

    while True:
        if len(gemdict.keys()) != gem_num:
            end += 1
            if end == len(gems):
                break
            gemdict[gems[end]] += 1
        else:
            if end-start < N:
                N = end-start
                answer = [start+1,end+1]
            gemdict[gems[start]] -= 1
            if gemdict[gems[start]] <= 0:
                gemdict.pop(gems[start])
            start += 1
    return answer

def solution1(gems):
    answer = []
    all_gem = set(gems)
    gem_num = len(all_gem)
    N = len(gems)
    start,end = 0,1

    if gem_num == 1:
        return [1,1]

    while start <= end:
        mid = (start+end) // 2
        here = checkPattern(gems,mid,N,gem_num)
        
        if here != int(1e9) and mid == gem_num:
            break
        if here == int(1e9):
            start = mid+1
        else:
            end = mid-1

    answer.append(here+1)
    answer.append(here+mid)
    return answer

def checkPattern(gems,dist,N,gem_num):
    i = 0
    while i+dist <= N:
        if len(set(gems[i:i+dist])) == gem_num:
            return i
        i += 1
    return int(1e9)

print(solution(["DIA", "EM", "EM", "RUB", "DIA"]))
print(solution(["A", "A", "B"]))
print(solution(["RUBY", "DIA", "EMERALD", "SAPPHIRE"]))
print(solution(["XYZ", "XYZ", "XYZ"]))