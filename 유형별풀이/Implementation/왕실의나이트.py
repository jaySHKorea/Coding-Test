'''
    행복 왕국의 왕실 정원은 8X8 평면이다. 특정한 칸에 나이트가 서있음
    나이트는 L자 형태로만 이동가능

    1. 수평으로 두 칸 이동한 뒤 수직 한 칸 이동
    2. 수직으로 두칸 이동한 뒤에 수평으로 한 칸 이동

    나이트의 위치가 주어졌을 때, 나이트가 이동할 수 있는 경우의 수를 출력하시오
    행은 1~8, 열은 a~h로 표현
'''

def knight(row,col):
    answer = 0
    move = [(2,-1),(1,-2),(-2,-1),(-1,-2),(-2,1),(-1,2),(2,1),(1,2)]

    for m in move:
        n_row = row+m[0]
        n_col = col+m[1]

        if ( n_row >= 1 and n_row <= 8 and n_col >= 1 and n_col <= 8 ):
            answer += 1
    return answer

if __name__ == '__main__':
    where = input()
    row = int(where[1])
    col = int(ord(where[0])) - int(ord('a')) + 1
    print(knight(row,col))