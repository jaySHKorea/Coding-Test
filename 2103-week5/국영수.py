'''
    정렬 01 - 국영수

    도현이네 반 학생 N명의 국,영,수 점수가 주어집니다. 다음과 같은 조건으로 학생의 성적을 정렬하는 프로그램을 작성하세요.

    1. 국어 점수가 감소하는 순서로
    2. 국어 점수가 같으면 영어점수가 증가하는 순서로
    3. 국어 점수와 영어 점수가 같으면 수학 점수가 감소하는 순서로
    4. 모든 점수가 같으면 이름이 사전으로 증가하는 순서로
'''
import sys

def solution(student):
    student = sorted(student,key=lambda x:(-x[1],x[2],-x[3],x[0]))
    
    for s in student:
        print(s[0])

if __name__ == '__main__':
    N = int(input())
    student = []
    for i in range(N):
        s = list(sys.stdin.readline().rstrip().split(" "))
        student.append([s[0],int(s[1]),int(s[2]),int(s[3])])
    solution(student)