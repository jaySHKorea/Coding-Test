# 프로그래머스 여행경로 : BFS/DFS
'''
주어진 항공권을 모두 이용하여 여행경로를 짜려고 합니다.
항상 ICN 공항에서 출발합니다.

항공권 정보가 담긴 2차원 배열 tickets가 매개변수로 주어질 때,
방문하는 공항 경로를 배열에 담아 return 하도록 solution 함수를 작성해주세요.
'''

#제한사항
'''
모든 공항은 알파벳 대문자 3글자로 이루어집니다.
주어진 공항 수는 3개 이상 10,000개 이하입니다.
tickets의 각 행 [a, b]는 a 공항에서 b 공항으로
가는 항공권이 있다는 의미입니다.
주어진 항공권은 모두 사용해야 합니다.
만일 가능한 경로가 2개 이상일 경우 알파벳 순서가 앞서는 경로를 return 합니다.
모든 도시를 방문할 수 없는 경우는 주어지지 않습니다.
'''

answer = []
cnt = 0

def solution(tickets):
    global answer
    tickets = sorted(tickets,key=lambda x: x[1])
    used = [False for col in range(len(tickets))]
    answer.append("ICN")
    dfs("ICN",tickets,used,-1)
    return answer

def dfs(where,tickets,used,prev):
    global answer
    global cnt
    cnt_m = cnt
    if ( cnt == len(tickets)):
        return
    for i in range(len(tickets)):
        if ( tickets[i][0] == where and used[i] == False):
            answer.append(tickets[i][1])
            used[i] = True
            cnt += 1
            dfs(tickets[i][1],tickets,used,i) # i는 경로취소에 사용
    
    # 일치하는게 없을 때 : 경로 취소
    if ( cnt == cnt_m ):
        answer.pop(-1) # answer에서 빼기
        used[prev] = False # 방문기록 삭제
        cnt -= 1 # 개수 빼기
        return 


#print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))
#print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
print(solution([["ICN", "A"], ["ICN", "B"], ["B", "ICN"]]))