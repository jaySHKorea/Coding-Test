'''
    정렬 03 - 실패율

    게임 개발중에 신규 사용자의 수가 급감했습니다. 원인은 신규 사용자와 기존 사용자 사이에 스테이지 차이가 너무 큰 것이 문제였습니다.
    이 문제에 대해서 동적으로 게임 시간을 늘려서 난이도를 조절하기로 했습니다.
    이때, 로직에 대해 실패율을 구하는 코드를 완성해 주세요.

    실패율 = (스테이지에 도달했으나 아직 클리어하지 못한 플레이어 수 / 스테이지에 도달한 플레이어 수)


'''
def solution(N, stages):
    answer = []
    stages.sort()
    count = [[0,0] for _ in range(N+1)]
    stages.append(-1)
    prev = stages[0]
    cnt = 1

    for i in range(1,len(stages)):
        if prev == stages[i]:
            cnt += 1
            continue
        check(N,prev,cnt,count)
        cnt = 1
        prev = stages[i]

    cal = []
    for i in range(1,N+1):
        if count[i][1] == 0:
            cal.append([i,0])
        else:
            cal.append([i,count[i][0]/count[i][1]])

    cal = sorted(cal,reverse=True,key=lambda x:x[1])
    for c in cal:
        answer.append(c[0])
    return answer

def check(N,i,cnt,count):
    # 도전자 갱신
    if i <= N:
        count[i][0] += cnt    
    # 클리어 갱신
    if i > N:
        i = N
    for j in range(1,i+1):
        count[j][1] += cnt

print(solution(5,[2, 1, 2, 6, 2, 4, 3, 3]))