'''
    구현
'''

def solution(numbers, hand):
    answer = ''
    pad = dict({"1":[0,0],"2":[0,1],"3":[0,2],"4":[1,0],"5":[1,1],"6":[1,2],"7":[2,0],"8":[2,1],"9":[2,2],"*":[3,0],"0":[3,1],"#":[3,2]})
    rhand = '#'
    lhand = '*'

    for number in numbers:
        if number in [1,4,7]:
            answer += 'L'
            lhand = str(number)
        elif number in [3,6,9]:
            answer += 'R'
            rhand = str(number)
        else:
            x,y = pad[str(number)]
            lx,ly = pad[lhand]
            rx,ry = pad[rhand]

            if abs(lx-x)+abs(ly-y) < abs(rx-x)+abs(ry-y):
                answer += 'L'
                lhand = str(number)
            elif abs(lx-x)+abs(ly-y) > abs(rx-x)+abs(ry-y):
                answer += 'R'
                rhand = str(number)
            else:
                if hand == 'right':
                    answer += 'R'
                    rhand = str(number)
                else:
                    answer += 'L'
                    lhand = str(number)

    return answer

print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5],"right"))