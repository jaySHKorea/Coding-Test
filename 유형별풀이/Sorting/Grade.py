'''
    N명의 학생 정보가 있다. 학생 정보는 학생 이름과 성적으로 구분된다.
    성적 정보를 성적이 낮은 순서대로 출력하시오
'''

if __name__ == '__main__':
    students = []
    N = int(input())
    for i in range(N):
        input_data = input().split()
        students.append((input_data[0], int(input_data[1])))
    students.sort(key=lambda student: student[1])
    for i in students:
        print(i[0], end=' ')