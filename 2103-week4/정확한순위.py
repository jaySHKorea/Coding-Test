'''
    최단경로 02 - 정확한 순위

    선생님은 시험을 본 학생 N명의 성적을 분실하고, 성적을 비교한 결과의 일부만 가지고 있다.
    학생 N명의 성적은 모두 다른데, 6번 비교한 기록이 있습니다.
'''
from collections import defaultdict
import sys

def solution(N,come,out):
    answer = 0
    
    for i in range(1,N+1):
        for grade in come[i]: # ex: 4(i)로 3(grade)이 들어온다 == 4의 앞순위들은 무조건 3의 앞에 있다 -> 3의 out(나가는 큐)에 4의 out(나가는 큐) 추가
            out[grade].update(out[i])
        for grade in out[i]: # ex: 1(i)이 5(grade)로 나간다 == 1의 뒤순위들은 무조건 5의 뒤에도 있다 -> 5의 come(들어오는 큐)에 1의 come(들어오는 큐) 추가
            come[grade].update(come[i])

    for i in range(1,N+1):
        if len(come[i]|out[i]) == N-1:
            answer += 1
    return answer

'''
def calculate(array,i):
    result = []
    for grade in array[i]:
        result.append(grade)
        result += array[grade]
    
    result = list(set(result))
    return result
'''
if __name__ == '__main__':
    N,M = map(int,sys.stdin.readline().rstrip().split(" "))
    out,come = defaultdict(set),defaultdict(set)

    for i in range(M):
        var = list(map(int,sys.stdin.readline().rstrip().split(" ")))
        come[var[1]].add(var[0])
        out[var[0]].add(var[1])
    print(solution(N,come,out))