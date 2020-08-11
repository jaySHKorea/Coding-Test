# 2019 카카오 개발자 겨울 인턴쉽 문제
# 문제 설명
"""
1. 5 < 문자열 s의 길이 < 1,000,000
2. s는 숫자와 '{','}',','로 이루어짐
3. 숫자가 0으로 시작하는 경우는 없음
4. s는 항상 중복되는 원소가 없는 튜플을 올바르게 표현함
5. s가 표현하는 튜플의 원소는 1 이상 100,000 이하의 자연수
6. return 하는 배열의 길이가 1 이상 500 이하인 경우만 입력으로 주어집니다.
"""

# python 문자열 관련 함수
"""
.split('') - 특정 문자로 나눈 뒤 1개의 리스트 반환
.join('')
"""

#import string

def solution(s):
    # 문자열 s가 표현하는 튜플
    answer = []
    clean_s = []

    # {{2}, {2, 1}, {2, 1, 3}, {2, 1, 3, 4}}

    # 2}, - temp[0]
    # 2, 1}, - temp[1]
    # 2, 1, 3}, - temp[2]
    # 2, 1, 3, 4}} - temp[3]

    # '{',',','}'를 기점으로 split
    split_s = s.split("{")

    for index in range(0,len(split_s)):
        if (split_s[index] != ''):
            split_s2 = split_s[index].replace(" ","").strip(',').replace("}","") # } 기호 삭제 
            clean_s.append([int(x) for x in split_s2.split(",")])

    # 리스트 길이(숫자 개수)에 따라 정렬
    clean_s.sort(key=lambda x: len(x))

    answer.append(clean_s[0][0])
    # 한거를 하나씩 따라가면서 answer에 추가
    for i in range(1,len(clean_s)):
        for j in range(0,len(clean_s[i])):
            if clean_s[i][j] not in answer:
                answer.append(clean_s[i][j])

    return answer


#s = "{{2},{2, 1},{2, 1, 3},{2, 1, 3, 4}}"
s = "{{1, 2, 3}, {2, 1}, {1, 2, 4, 3}, {2}}"
print(solution(s))
