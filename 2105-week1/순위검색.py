'''
    코딩테스트 참여 개발언어 항목에 cpp, java, python 중 하나를 선택해야 합니다.
    지원 직군 항목에 backend와 frontend 중 하나를 선택해야 합니다.
    지원 경력구분 항목에 junior와 senior 중 하나를 선택해야 합니다.
    선호하는 소울푸드로 chicken과 pizza 중 하나를 선택해야 합니다.

    [조건]을 만족하는 사람 중 코딩테스트 점수를 X점 이상 받은 사람은 모두 몇 명인가?


'''

def solution(info, query):
    answer = []
    db = dict({"java":set(),"cpp":set(),"python":set(),
                "frontend":set(),"backend":set(),
                "junior":set(),"senior":set(),
                "chicken":set(),"pizza":set(),"-":set(list(range(len(info))))})
    score = []
    N = len(info)
    
    for i,inn in enumerate(info):
        a = inn.split(" ")
        score = int(a.pop(-1))
        info[i] = [a,score]

    info = sorted(info,key=lambda x:x[1])
    db = makedict(info,db)

    for q in query:
        #q = q.replace("and ","")
        #conds = q.split(" ")
        conds = q.split(" and ")
        conds.extend(conds.pop().split(" "))
        score = int(conds.pop(-1))
        here = binary_search(info,score,0,N-1)
        inter = set(i for i in range(here,N))

        inter = inter & db[conds[0]]& db[conds[1]]& db[conds[2]]& db[conds[3]]
        answer.append(len(inter))
    return answer

def makedict(info,db):
    for i,inn in enumerate(info):
        for cond in inn[0]:
                db[cond].add(i)
    return db

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start+end) // 2

        if array[mid-1][1] < target and array[mid][1] >= target:
            return mid
        elif array[mid][1] >= target:
            end = mid - 1
        else:
            start = mid + 1
    return start

print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))