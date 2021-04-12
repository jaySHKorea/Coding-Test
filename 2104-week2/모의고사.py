'''
    프로그래머스 완전탐색 - 모의고사
'''

def solution(answers):
    answer = []
    cnt = [[1,0],[2,0],[3,0]]
    one = [1,2,3,4,5]
    two = [2,1,2,3,2,4,2,5]
    three = [3,3,1,1,2,2,4,4,5,5]

    for i,ans in enumerate(answers):
        if ans == one[i%5]:
            cnt[0][1] += 1
        if ans == two[i%8]:
            cnt[1][1] += 1
        if ans == three[i%10]:
            cnt[2][1] += 1
    
    cnt = sorted(cnt,reverse=True,key=lambda x:x[1])
    answer.append(cnt[0][0])
    
    for i in range(1,3):
        if cnt[0][1] == cnt[i][1]:
            answer.append(cnt[i][0])
        else:
            break
    answer.sort()

    return answer