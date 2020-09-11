# 프로그래머스 조이스틱 : 탐욕법(Greedy)

'''
조이스틱으로 알파벳 이름을 완성하세요. 맨 처음엔 A로만 이루어져 있습니다.
ex) 완성해야 하는 이름이 세 글자면 AAA, 네 글자면 AAAA

▲ - 다음 알파벳
▼ - 이전 알파벳 (A에서 아래쪽으로 이동하면 Z로)
◀ - 커서를 왼쪽으로 이동 (첫 번째 위치에서 왼쪽으로 이동하면 마지막 문자에 커서)
▶ - 커서를 오른쪽으로 이동

- 첫 번째 위치에서 조이스틱을 위로 9번 조작하여 J를 완성합니다.
- 조이스틱을 왼쪽으로 1번 조작하여 커서를 마지막 문자 위치로 이동시킵니다.
- 마지막 위치에서 조이스틱을 아래로 1번 조작하여 Z를 완성합니다.
따라서 11번 이동시켜 "JAZ"를 만들 수 있고, 이때가 최소 이동입니다.
'''

# 제한사항
'''
name은 알파벳 대문자로만 이루어져 있습니다.
name의 길이는 1 이상 20 이하입니다.
'''

# 기본 함수 정보 참고 : https://wikidocs.net/32
# A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
def solution(name):
    answer = 0
    name=list(name) # 한글자씩 리스트화
    index=0

    while(True):
        right=1
        left=1
        # 위아래 버튼 이동
        if ( name[index] != 'A' ): #문자가 A가 아니라면 
            updown = min(ord(name[index])-ord('A'),(ord('Z')-ord(name[index])+1)) # 위/아래 중 더 빠른 곳 찾기
            answer += updown #add
        name[index] = 'A'
        # 완료 시점
        if ( name == ["A"]*len(name)): #name이 A의 반복이라면( 입력 완료 )
            break
        # 좌우 버튼(커서) 이동
        for i in range(1,len(name)):
            if name[index+i]=="A": right+=1 # 커서 뒤로 A가 아닌 입력 문자까지의 이동 : right 버튼 클릭수
            else: break
        for i in range(1,len(name)):
            if name[index-i]=="A": left+=1 # 커서 앞으로 A가 아닌 입력 문자까지의 이동 : left 버튼 클릭수
            else: break
        if ( right>left ): # 커서를 왼쪽버튼으로 가는게 더 빠르다
            answer+=left
            index-=left # 왼쪽으로 커서 이동
        else: # 오른쪽버튼이 더 빠르다(횟수가 작다)
            answer+=right
            index+=right # 오른쪽으로 커서 이동
    return answer

solution("JEROEN")	#56
solution("JAN")     #23