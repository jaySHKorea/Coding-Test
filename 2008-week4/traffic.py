# 2020 kakao blind recruitment
'''
이번 추석에도 시스템 장애가 없는 명절을 보내고 싶은 어피치는 서버를 증설해야 할지 고민이다.
장애 대비용 서버 증설 여부를 결정하기 위해 작년 추석 기간인 9월 15일 로그 데이터를 분석한 후 초당 최대 처리량을 계산해보기로 했다.
초당 최대 처리량은 요청의 응답 완료 여부에 관계없이 임의 시간부터 1초(=1,000밀리초)간 처리하는 요청의 최대 개수를 의미한다.

solution 함수에 전달되는 lines 배열은 N(1 ≦ N ≦ 2,000)개의 로그 문자열로 되어 있으며, 
각 로그 문자열마다 요청에 대한 응답완료시간 S와 처리시간 T가 공백으로 구분되어 있다.
응답완료시간 S는 작년 추석인 2016년 9월 15일만 포함하여 고정 길이 2016-09-15 hh:mm:ss.sss 형식으로 되어 있다.
처리시간 T는 0.1s, 0.312s, 2s 와 같이 최대 소수점 셋째 자리까지 기록하며 뒤에는 초 단위를 의미하는 s로 끝난다.
예를 들어, 로그 문자열 2016-09-15 03:10:33.020 0.011s은 
2016년 9월 15일 오전 3시 10분 **33.010초**부터 2016년 9월 15일 오전 3시 10분 **33.020초**까지 **0.011초** 동안 처리된 요청을 의미한다. (처리시간은 시작시간과 끝시간을 포함)
서버에는 타임아웃이 3초로 적용되어 있기 때문에 처리시간은 0.001 ≦ T ≦ 3.000이다.
lines 배열은 응답완료시간 S를 기준으로 오름차순 정렬되어 있다.
'''

# solution 함수에서는 로그 데이터 lines 배열에 대해 초당 최대 처리량을 리턴한다.

from datetime import datetime, timedelta
import datetime
import collections
 
# 1초는 999ms
def solution(lines):
    bar = collections.namedtuple('bar', 'time se') # 시각 / 시작시간 or 마침시간 인지
    answer = 0
    now = 0
    bar_data = []

    # 문자열 parsing 2016-09-15 hh:mm:ss.sss 2.0s
    for i in range(0,len(lines)):
        clean = lines[i].split(" ") # 0 : 날짜, 1 : 시간분, 2 : 처리시간
        # 연도 날짜
        year_day = list(map(int,clean[0].split("-")))
        # 시간분
        hour_to_micro = clean[1].split(":")
        sec_to_mircro = hour_to_micro[2].split(".")
        hour_to_micro = list(map(int,hour_to_micro[0:2]))
        sec_to_mircro = list(map(int,sec_to_mircro))
        # 처리시간
        clean[2] = clean[2].replace("s","")
        clean[2] = float(clean[2])

        end = datetime.datetime(year_day[0],year_day[1],year_day[2],hour_to_micro[0],hour_to_micro[1],sec_to_mircro[0],sec_to_mircro[1]*1000)
        start = end - timedelta(seconds=clean[2])
        # 배열에 넣기
        bar_data.append(bar(time=start,se=0))
        bar_data.append(bar(time=end+timedelta(microseconds=999999),se=1)) # end 시각으로터 1초 안에 있으면 같은 작업 단위라서


    # 오름차순 시간에 맞춰서 정렬하기
    bar_data = sorted(bar_data, key = lambda x : x.time)
    #print(bar_data)

    for i in range(0,len(bar_data)):
        if ( bar_data[i].se == 0): # start라면 : 작업 시작
            now += 1
        else: # end 라면 : 작업종료
            now -= 1
        if ( answer < now ): answer = now

    return answer

lines =  [
"2016-09-15 20:59:57.421 0.351s",
"2016-09-15 20:59:58.233 1.181s",
"2016-09-15 20:59:58.299 0.8s",
"2016-09-15 20:59:58.688 1.041s",
"2016-09-15 20:59:59.591 1.412s",
"2016-09-15 21:00:00.464 1.466s",
"2016-09-15 21:00:00.741 1.581s",
"2016-09-15 21:00:00.748 2.31s",
"2016-09-15 21:00:00.966 0.381s",
"2016-09-15 21:00:02.066 2.62s"
]

print(solution(lines))