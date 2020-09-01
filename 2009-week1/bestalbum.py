# Hash 문제
'''
스트리밍 사이트에서 장르 별로 가장 많이 재생된 노래를 
"두 개씩" 모아 베스트 앨범을 출시하려 합니다.
노래는 고유 번호로 구분하며, 노래를 수록하는 기준은 다음과 같습니다.

속한 노래가 많이 재생된 장르를 먼저 수록합니다.
장르 내에서 많이 재생된 노래를 먼저 수록합니다.
장르 내에서 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 노래를 먼저 수록합니다.
노래의 장르를 나타내는 문자열 배열 genres와 노래별 재생 횟수를 나타내는 정수 배열 plays가 주어질 때,
베스트 앨범에 들어갈 노래의 고유 번호를 순서대로 return 하도록 solution 함수를 완성하세요.

제한사항
genres[i]는 고유번호가 i인 노래의 장르입니다.
plays[i]는 고유번호가 i인 노래가 재생된 횟수입니다.
genres와 plays의 길이는 같으며, 이는 1 이상 10,000 이하입니다.
장르 종류는 100개 미만입니다.
장르에 속한 곡이 하나라면, 하나의 곡만 선택합니다.
모든 장르는 재생된 횟수가 다릅니다.
'''

import collections

def solution(genres, plays):
    answer = []
    #song = collections.namedtuple('song', 'genre play index')
    #song_sum = collections.namedtuple('songsum','genre sum')
    album = []
    album_sum = []

    # 배열 만들기
    for i in range(0,len(genres)):
        flag = False
        # genre별 play 합 계산
        for j in range(0,len(album_sum)):
            if ( album_sum[j][0] == genres[i] ):
                album_sum[j][1] += plays[i]
                flag = True
                break
        if ( flag == False):
            album_sum.append([genres[i],plays[i]])
        album.append([genres[i],plays[i],i])

    album_sum = sorted(album_sum, key=lambda album: album[1], reverse=True)
    album = sorted(album, key=lambda song: song[1], reverse=True) # play 횟수로 정렬

    for i in range(0,len(album_sum)):
        cnt = 0
        for j in range(0,len(album)):
            if ( cnt == 2 ):break
            if ( album[j][0] == album_sum[i][0]):
                answer.append(album[j][2])
                cnt += 1
    
    return answer

solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500])