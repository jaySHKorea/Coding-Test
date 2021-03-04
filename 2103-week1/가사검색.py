'''
    2020 카카오 신입공채 - 가사 검색

    노래 가사에 사용된 단어들 중에 특정 키워드가 몇 개 포함되어있는지 궁금하니 개발해달라는 제안
    키워드는 와일드카드 문자 중 하나인 ?가 포함된 패턴 형태의 문자열을 뜻합니다.

    와일드카드 문자인 ?는 글자 하나를 의미하며, 어떤 문자에도 매치된다고 가정합니다.

    가사에 사용된 모든 단어들이 담긴 배열 words 와 찾고자 하는 키워드가 담긴 배열 queries가 주어질 때,
    각 키워드 별로 매치된 단어가 몇 개인지 순서대로 배열에 담아 반환하도록 solution을 작성하세요.
'''    
# 1 : words들을 길이 별로 정리하고 전체 탐색
# 2 : 단어들을 길이 별로 trie를 만들고 탐색, 이때 트라이는 양 방향으로 두개씩 생성

class Node:
    def __init__(self, char, data = None):
        # 노드의 글자
        self.char = char
        # 마지막 노드일 때 string 값
        self.data = data
        # 해당 노드를 거쳐갈 경우 가능한 글자의 개수
        self.possible_word = 0
        # trie의 자식 노드들
        self.children = {}

class Trie:
    def __init__(self):
        self.head = Node(None)

    def insert(self, string):
        curr_node = self.head
        for char in string:
            # 노드의 가능한 글자 개수 플러스
            curr_node.possible_word += 1
            if char not in curr_node.children:
                # 해당 노드의 next에 문자열이 등록되어 있지 않으면 등록한다.
                curr_node.children[char] = Node(char)
            # 다음 노드로 이동
            curr_node = curr_node.children[char]
        
        # 마지막 글자에 도착
        curr_node.possible_word += 1
        curr_node.data = string # 최종완성문자 저장해두기

    def search(self, string):
        curr_node = self.head
        for char in string:
            #노드를 타고 내려가기
            if char in curr_node.children:
                curr_node = curr_node.children[char]
            else:
                return 0
            
        # 해당 노드까지 왔을 때 만들 수 있는 문자의 개수가 1이면 True 반환
        return curr_node.possible_word


def solution(words, queries):
	answer = []

	trie = [ Trie() for i in range(10000)] 
	reverse = [ Trie() for i in range(10000)]

	for w in words:
		trie[len(w)-1].insert(w)
		reverse[len(w)-1].insert(w[::-1])

	for query in queries:
		flag = False
		if query[0] == '?' and query[-1] != '?': # ?로 시작하는 키워드 뒤집어주기
			flag = True
			query = query[::-1]

		pre=0
		for idx,c in enumerate(query):
			if c == '?': 
				pre = idx
				break

		if flag:
			answer.append(reverse[len(query)-1].search(query[:pre]))
		else:
			answer.append(trie[len(query)-1].search(query[:pre]))

	return answer

print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"],["fro??", "????o", "fr???", "fro???", "pro?"]))
'''
import re

def solution(words, queries):
    answer = []

    gasa = [[] for _ in range(10001)]

    # 가사를 단어길이 별로 정리
    for w in words:
        gasa[len(w)].append(w)

    for q in queries:
        here = gasa[len(q)]
        cnt = 0
        end,start = 0,-1

        for i in range(len(q)):
            if (q[i] == '?'):
                if ( start == -1 ): # 처음 나온 물음표
                    start = i
                else:
                    end = i
        if ( end == 0 ): end = len(q)-1

        # 다 물음표인 경우
        if end-start == len(q)-1:
            answer.append(len(here))
        elif start == 0:
            for h in here:
                if re.search(q[end+1:]+'$',h):
                    cnt += 1
            """
            for h in here:
                if ( h[end+1:] == q[end+1:]):
                    cnt += 1
            """
            answer.append(cnt)
        elif end == len(q)-1:
            for h in here:
                if re.search('^'+q[:start],h):
                    cnt += 1
            """
            for h in here:
                if ( h[:start] == q[:start]):
                    cnt += 1
            """
            answer.append(cnt)
    return answer
'''
