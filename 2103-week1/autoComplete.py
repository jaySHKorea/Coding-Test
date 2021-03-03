'''
    2018 카카오 blind 채용 - 자동완성
    https://programmers.co.kr/learn/courses/30/lessons/17685?language=python3

    한 번 입력된 문자열을 학습해서 다음 입력 때 활용한다.
    예를 들어 go가 한 번 입력되었다면, 다음 사용자는 g만 입력해도 go를 추천해주므로 o를 입력할 필요가 없다.
    단, 학습에 사용된 단어들 중 앞부분이 같은 경우에는 어쩔 수 없이 다른 문자가 나올 때까지 입력을 해야한다.
    효과가 얼마나 좋을지 알고 싶은 라이언은 특정 학습된 단어를 찾기위해 몇글자를 입력해야하는 궁금해졌다.

    학습/검색에 사용될 중복 없는 단어 N개가 주어진다.
    모든 단어는 알파벳 소문자로 구성되며, 단어의 수 N과 길이의 총합 L의 범위는 다음과 같다.

    단어를 찾을 때 입력해야 할 총 문자수를 리턴한다.
'''

# 트라이(trie) 문제 - 더이상 단어의 분기점이 없는 지점을 찾아라

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
                return False
            
        # 해당 노드까지 왔을 때 만들 수 있는 문자의 개수가 1이면 True 반환
        if curr_node.possible_word == 1:
            return True
        else:
            return False

    def start_with(self, prefix):
        curr_node = self.head
        result = []
        for char in prefix:
            if char in curr_node.children:
                 curr_node = curr_node.children[char]
                 subtrie = curr_node
            else:
                return []

        stack = list(subtrie.children.values())

        # dfs로 단어 완성
        while stack:
            node = stack.pop()
            if node.data != None:
                result.append(node.data)
            stack.extend(list(node.children.values()))
        return result 

def solution(words):
    answer = 0

    word_trie = Trie()
    for word in words:
        word_trie.insert(word)

    for word in words:
        already_find = False
        for i in range(1, len(word)+1):
            if word_trie.search(word[:i]):
                answer += len(word[:i])
                already_find = True
                break
        if not already_find:
            answer += len(word)
    return answer

solution(["go","gone","guild"])