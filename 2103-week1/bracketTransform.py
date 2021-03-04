'''
    43m

    2020 카카오 신입 공채
    ( )가 모두 있을 때, 각 괄호의 개수가 같다면 이를 균형잡힌 괄호 문자열이라고 부른다.
    이때, ( )의 괄호의 짝도 모두 맞을 경우에는 이를 올바른 괄호 문자열이라고 부릅니다.

    어떤 균형잡힌 괄호 문자열이 있을 때 다음 과정을 통해 올바른 괄호 문자열로 변환할 수 있습니다.
    1. 입력이 빈 문자열이라면 빈 문자열을 반환합니다.
    2. 문자열 w를 두 균형잡힌 괄호 문자열 u,v로 분리합니다. 이때 u는 더이상 분리할 수 없는 균형잡힌 괄호 문자열이며, v는 빈 문자열이 될 수 있습니다.
    3. 문자열 u가 올바른 괄호 문자열이라면 문자열 v에 대해 1단계부터 다시 수행합니다.
    4. 문자열 u가 올바른 괄호 문자열이 아닐 경우
        41. 빈 문자열에 첫 번째 문자로 ( 를 붙입니다.
        42. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙입니다.
        43. )를 다시 붙입니다.
        44. u의 첫번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다.
'''

def solution(p):
    return separate(p)

def separate(string):
    temp = ''

    # 빈 문자열이라면 빈문자열을 반환 
    if string == '':
        return ''

    left_cnt = 0
    right_cnt = 0
    sList = list(string)

    # u,v 분리
    for i in range(len(sList)):
        if ( sList[i] == '('):
            left_cnt += 1
        else:
            right_cnt += 1
        if ( left_cnt == right_cnt ):
            break
    
    u,v = string[:i+1],string[i+1:]

    # 올바른 문자열인 경우
    if check(u):
        temp += u
        if ( v != ''):
            temp += separate(v)
    # 올바른 문자열이 아닌 경우
    else:
        temp = '('
        temp += separate(v)
        temp += ')'
        for i in range(1,len(u)-1):
            if u[i] == '(':
                temp += ')'
            else:
                temp += '('
    return temp

# 올바른 문자열인지 확인
def check(string):
    left_cnt = 0
    right_cnt = 0
    sList = list(string)

    for s in sList:
        if ( s == '('):
            left_cnt += 1
        else:
            right_cnt += 1
        if ( right_cnt > left_cnt):
            return False
    return True
    
print(solution('()))((()'))