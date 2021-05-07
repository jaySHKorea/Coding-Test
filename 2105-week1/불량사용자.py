from typing import DefaultDict
import itertools

def solution(user_id, banned_id):
    answer = 0
    banned = dict()

    for ban in banned_id:
        if ban in banned.keys():
            continue
        else:
            banned[ban] = []
        if '*'*len(ban) == ban:
            for user in user_id:
                if len(user) == len(ban):
                    banned[ban].append(user)
            continue        
        for user in user_id:
            flag = 1
            if len(ban) != len(user):
                continue
            for i,ch in enumerate(user):
                if ban[i] == '*':
                    continue
                if ch != ban[i]:
                    flag = 0
                    break
            if flag == 1:
                banned[ban].append(user)

    case = 1
    for key in banned_id:
        case *= len(banned[key])

    allcase = [[] for _ in range(case)]
    answer = case

    prev = 1
    for key in banned_id:
        i = 0
        lenn = int(case/len(banned[key]))
        for k in range(0,prev):
            for ban in banned[key]:
                for j in range(i,i+lenn):
                    allcase[j].append(ban)
                i += lenn
        prev *= len(banned[key])
        case = lenn
    
    result = []
    for c in allcase:
        if len(set(c)) != len(banned_id):
            answer -= 1
        elif set(c) in result:
            answer -= 1
        else:
            result.append(set(c))
    
    return answer

print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],["fr*d*", "*rodo", "******", "******"]))
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],["*rodo", "*rodo", "******"]))