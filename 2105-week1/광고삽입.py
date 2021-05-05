'''
    카카오 21 공채 - 광고 삽입 < 투포인터, 누적합 >

    
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
    play_sec = toSecond(play_time) # 전체 플레이타임
    adv_sec = toSecond(adv_time) # 광고 시간
    ad = [0 for _ in range(360001)]

    # 광고의 시작, 끝 표시
    for log in logs:
        sep = log.split("-")
        ad[toSecond(sep[0])] += 1
        ad[toSecond(sep[1])] -= 1
    
    # 각 구간 재생횟수
    for idx in range(1,play_sec+1):
        ad[idx] += ad[idx-1]
    # 누적합
    for idx in range(1,play_sec+1):
        ad[idx] += ad[idx-1]
    
    max_time = 0
    max_played = ad[adv_sec]
    # 1초씩 한칸씩 밀어서 시간 계산
    for start in range(1,play_sec):
        end = start + adv_sec if start + adv_sec < play_sec else play_sec
        play = ad[end]-ad[start] # 구간 누적합 구하기
        if max_played < play:
            max_played = play
            max_time = start+1 #end-start이기 때문에
	
    answer = toString(max_time)
    return answer

print(solution("02:03:55","00:14:15",["01:20:15-01:45:14", "01:30:59-01:53:29", "01:37:44-02:02:30"]))