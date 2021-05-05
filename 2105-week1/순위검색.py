'''
    query 구현문제

    < 모든 검색 조건에 대한 정렬된 score 리스트 생성, 구해서 점수 조건에 대해 이진탐색으로 구하기 >
    
    코딩테스트 참여 개발언어 항목에 cpp, java, python 중 하나를 선택해야 합니다.
    지원 직군 항목에 backend와 frontend 중 하나를 선택해야 합니다.
    지원 경력구분 항목에 junior와 senior 중 하나를 선택해야 합니다.
    선호하는 소울푸드로 chicken과 pizza 중 하나를 선택해야 합니다.

    [조건]을 만족하는 사람 중 코딩테스트 점수를 X점 이상 받은 사람은 모두 몇 명인가?


'''
import bisect

def solution(info, query):
    answer = []

    db = dict({"java":set(),"cpp":set(),"python":set(),
                "frontend":set(),"backend":set(),
                "junior":set(),"senior":set(),
                "chicken":set(),"pizza":set(),"-":set(list(range(len(info))))})
    
    # 세부조건 dictionary 만들기
    for i,inn in enumerate(info):
        info[i] = inn.split(" ")
        info[i][-1] = int(info[i][-1])

        db[info[i][0]].add(i)
        db[info[i][1]].add(i)
        db[info[i][2]].add(i)
        db[info[i][3]].add(i)

    # 검색 조건의 모든 경우의 수에 대응하는 점수리스트 dictionary
    total_query_dict = makeTotalDict(db,info)

    # NlogN
    for q in query:
        conds = [_ for _ in q.split(' ') if _ != 'and']
        score = int(conds[-1])
        q = ' '.join(conds[:4])
        temp = total_query_dict[q]
        answer.append(len(temp)-bisect.bisect_left(temp,score)) # 점수 조건 이외 개수에서 만족하지 않는 개수의 차
    return answer

# 4*3*3*3*N 고정
def makeTotalDict(db,info):
    total_query_dict = dict()
    for lang in ['java','python','cpp','-']:
        for task in ['backend','frontend','-']:
            for career in ['junior','senior','-']:
                for food in ['pizza', 'chicken','-']:
                    temp = [info[i][-1] for i in list(db[lang]& db[task]& db[career]& db[food])]
                    total_query_dict[f'{lang} {task} {career} {food}'] = sorted(temp)
    return total_query_dict

def solution1(info, query):
    scores = []
    answer = []
    db = dict({"java":set(),"cpp":set(),"python":set(),
                "frontend":set(),"backend":set(),
                "junior":set(),"senior":set(),
                "chicken":set(),"pizza":set(),"-":set(list(range(len(info))))})
    N = len(info)
    
    # N
    for i,inn in enumerate(info):
        info[i] = inn.split(" ")
        score = int(info[i].pop(-1))
        scores.append([i,score])

        db[info[i][0]].add(i)
        db[info[i][1]].add(i)
        db[info[i][2]].add(i)
        db[info[i][3]].add(i)

    # NlogN
    scores = sorted(scores,key=lambda x:x[1])

    # N^2
    for q in query:
        conds = [_ for _ in q.split(' ') if _ != 'and']
        score = int(conds[-1])

        here = bisect.bisect_left(scores,score)
        inter = set([scores[i][0] for i in range(here,N)])

        inter = inter & db[conds[0]]& db[conds[1]]& db[conds[2]]& db[conds[3]]
        answer.append(len(inter))
    return answer

def solution2(info, query):
    answer = []
    info_list = []
    scores = []
    N = len(info)

    # N
    for i,inn in enumerate(info):
        info_list.append(inn.split(' '))
        score = int(info_list[i][-1])
        scores.append([i,score])

    # NlogN
    scores = sorted(scores,key=lambda x:x[1])
    
    # N^2
    for q in query:
        split_query = [_ for _ in q.split(' ') if _ != 'and']
        here = bisect.bisect_left(scores,score)

        res = [info_list[scores[i][0]] for i in range(here,N)
               if (split_query[0] =='-' or split_query[0] == info_list[scores[i][0]][0])
               and (split_query[1] == '-' or split_query[1] == info_list[scores[i][0]][1])
               and (split_query[2] == '-' or split_query[2] == info_list[scores[i][0]][2])
               and (split_query[3] == '-' or split_query[3] == info_list[scores[i][0]][3])
               ]
        answer.append(len(res))
    return answer

print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))