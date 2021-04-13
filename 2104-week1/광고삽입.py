'''
    카카오 21 공채 - 광고 삽입
    
    광고 효과를 높이기 위해 시청자들이 가장 많이 보는 구간에 공익광고를 넣으려고 합니다. 죠르디는 시청자들이 해당 동영상의
    어떤 구간을 재생했는지 알 수 있는 재생구간 기록을 구했고, 해당 기록을 바탕으로 공익광고가 삽입될 최적의 위치를 고를 수 있었습니다.
    참고로, 광고는 재생 중인 동영상의 오른쪽 아래에서 원래 영상과 동시 재생됩니다.
'''

def toSecond(string):
    result = 0
    s = string.split(":")
    result += int(s[0])*60*60+int(s[1])*60+int(s[2])
    return result

def toString(time):
    result = ''
    s = time%60
    time = int(time/60)
    m = time%60
    time = int(time/60)
    h = time

    if h < 10:
        result += '0'
    result += str(h)+":"
    if m < 10:
        result += '0'
    result += str(m)+":"
    if s < 10:
        result += '0'
    result += str(s)

    return result

# 투 포인터
def solution(play_time, adv_time, logs):
    answer = ''
    ad = [0 for _ in range(360001)]

    # 1초마다 순간에 몇 개의 광고가 있는지 표시
    for log in logs:
        sep = log.split("-")
        start = toSecond(sep[0])
        finish = toSecond(sep[1])
        for i in range(start,finish):
            ad[i] += 1

    N = toSecond(play_time) # 전체 플레이타임
    lenn = toSecond(adv_time) # 광고 시간
    idx = 0
    sum = 0
	
    q = []

    # 0초(처음)부터 광고를 상영할 때 총 광고가 시청자들에게 보여진 시간
    for i in range(0,lenn):
        sum += ad[i]
        q.append(ad[i])
    maxSum = sum

    # 1초씩 한칸씩 밀어서 시간 계산
    for i in range(lenn,N):
        sum += ad[i]
        q.append(ad[i])
        sum -= q[0] # 맨 앞의 1초의 상영한 사람수
        q.pop(0) # 큐에서 삭제
        if sum > maxSum:
            idx = i-lenn+1
            maxSum = sum
	
    answer = toString(idx)
    return answer

print(solution("02:03:55","00:14:15",["01:20:15-01:45:14", "01:30:59-01:53:29", "01:37:44-02:02:30"]))