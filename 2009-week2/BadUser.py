# 프로그래머스 불량사용자

# 제한 사항
'''
user_id 배열의 크기는 1 이상 8 이하입니다.
user_id 배열 각 원소들의 값은 길이가 1 이상 8 이하인 문자열입니다.
응모한 사용자 아이디들은 서로 중복되지 않습니다.
응모한 사용자 아이디는 알파벳 소문자와 숫자로만으로 구성되어 있습니다.
banned_id 배열의 크기는 1 이상 user_id 배열의 크기 이하입니다.
banned_id 배열 각 원소들의 값은 길이가 1 이상 8 이하인 문자열입니다.
불량 사용자 아이디는 알파벳 소문자와 숫자, 가리기 위한 문자 '*' 로만 이루어져 있습니다.
불량 사용자 아이디는 '*' 문자를 하나 이상 포함하고 있습니다.
불량 사용자 아이디 하나는 응모자 아이디 중 하나에 해당하고 같은 응모자 아이디가 중복해서
제재 아이디 목록에 들어가는 경우는 없습니다.
제재 아이디 목록들을 구했을 때 아이디들이 나열된 순서와 관계없이
아이디 목록의 내용이 동일하다면 같은 것으로 처리하여 하나로 세면 됩니다.
'''
import re
import copy

a_case = []

def solution(user_id, banned_id):
    global a_case
    case = []
    u_occ = [False for col in range(len(user_id))]
    b_occ = [-1 for col in range(len(banned_id))]
    #queue = deque([])

    # 정규표현식 .(\n 제외 문자와 매치)
    banned_id = [bid.replace("*",".") for bid in banned_id]

    # case 배열 만들기 : 각 불량 사용자가 어디 밴 아이디에 해당하는지
    for uid in user_id:
        tmp = []
        for i in range(len(banned_id)):
            bid = banned_id[i]
            p = re.compile(bid)
            if ( p.match(uid) and (len(bid) == len(uid))):
                tmp.append(i)
        case.append(tmp)

    # 가능한 경우의 수 찾기
    dfs(0,case,u_occ,b_occ)
    # 경우의수 리스트 정렬 후 중복 제거
    a_case = [sorted(a) for a in a_case]
    a_case = list(set(map(tuple,a_case)))

    return len(a_case)

def dfs(ban_idx,case,u_occ,b_occ):
    global a_case
    if ( ban_idx == len(b_occ) ):
        a_case.append(copy.deepcopy(b_occ))
        return
    for i in range(0,len(case)):
        if ( ban_idx in case[i] and b_occ[ban_idx] == -1 and u_occ[i] == False):
            b_occ[ban_idx] = i
            u_occ[i] = True
            dfs(ban_idx+1,case,u_occ,b_occ)
            u_occ[i] = False
            b_occ[ban_idx] = -1


print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"]))
#print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"]))
#print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"]))