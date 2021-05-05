# dp + dfs

dp = [[0,0] for _ in range(300001)]
team = [[] for _ in range(300001)]

def solution(sales, links):
    answer = 0

    for leader,emp in links:
        team[leader].append(emp)

    dfs(1,sales)
    return dp[1][1] if dp[1][0] > dp[1][1] else dp[1][0]

def dfs(now,sales):
    # 현재 노드 워크숍 참여
    dp[now][1] = sales[now-1]

    if team[now] != []:
        for node in team[now]:
            dfs(node,sales)

        minval = int(1e9)
        for node in team[now]:
            if dp[node][0] < dp[node][1]:
                dp[now][0] += dp[node][0]
                dp[now][1] += dp[node][0]
                minval = dp[node][1] - dp[node][0] if minval > dp[node][1] - dp[node][0] else minval
            else:
                dp[now][0] += dp[node][1]
                dp[now][1] += dp[node][1]
                minval = 0
        if minval != int(1e9):
            dp[now][0] += minval

'''
answer = int(1e9)
def solution(sales, links):
    team = dict()
    team_nums = []

    for leader,emp in links:
        if leader in team.keys():
            team[leader].append([emp,sales[emp-1]])
        else:
            team[leader] = [[emp,sales[emp-1]]]
            team_nums.append(leader)
    
    team_nums.sort()

    dfs(sales,team,team_nums,0,'',0)
    return answer

def dfs(sales,team,team_nums,i,copy,summ):
    global answer

    # 모든 조직 참석 완료
    if i >= len(team_nums):
        answer = min(answer,summ)
        return

    team_num = team_nums[i]

    # 이미 참석한 조직
    if str(team_num) in copy:
        dfs(sales,team,team_nums,i+1,copy,summ)
        return

    # 부서의 팀장이 참석한다.
    if summ+sales[team_num-1] < answer:
        dfs(sales,team,team_nums,i+1,copy+str(team_num),summ+sales[team_num-1])

    # 부서의 팀원이 참석한다.
    for emp,sale in team[team_num]:
        if summ+sale < answer:
            if emp in team.keys():
                dfs(sales,team,team_nums,i+1,copy+str(team_num)+str(emp),summ+sale)
            else:
                dfs(sales,team,team_nums,i+1,copy+str(team_num),summ+sale)

    return answer
'''
print(solution([14, 17, 15, 18, 19, 14, 13, 16, 28, 17],[[10, 8], [1, 9], [9, 7], [5, 4], [1, 5], [5, 10], [10, 6], [1, 3], [10, 2]]))