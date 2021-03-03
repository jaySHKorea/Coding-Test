'''
    구현 08 문자열 재정렬

    알파벳 대문자와 숫자(0~9)로만 구성된 문자열이 입력으로 주어진다. 이때 모든 알파벳을 오름차순으로 정렬하여 이어서 출력하고, 그 뒤에 모든 숫자를
    더한 값을 출력한다.
'''
import re

def solution(string):
    numbers = list(map(int,re.findall("\d", string))) # 뒤에 +추가하면 여러자리 수로 판단함
    strings = list(re.findall("[A-Z]",string))
    strings.sort() # sorted는 원래 변수에 소팅되서 저장되지 않음
    return ''.join(strings)+str(sum(numbers))

print(solution('K1KA5CB7'))
print(solution('AJKDLSI412K4JSJ9D'))


