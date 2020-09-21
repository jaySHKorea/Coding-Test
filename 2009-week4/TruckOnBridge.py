# 프로그래머스 다리를 지나는 트럭 : 스택/큐
'''
트럭 여러 대가 강을 가로지르는 일 차선 다리를 정해진 순으로 건너려 합니다.
모든 트럭이 다리를 건너려면 최소 몇 초가 걸리는지 알아내야 합니다.
트럭은 1초에 1만큼 움직이며, 다리 길이는 bridge_length이고 다리는 무게 weight까지 견딥니다.
※ 트럭이 다리에 완전히 오르지 않은 경우, 이 트럭의 무게는 고려하지 않습니다.

예를 들어, 길이가 2이고 10kg 무게를 견디는 다리가 있습니다.
무게가 [7, 4, 5, 6]kg인 트럭이 순서대로 최단 시간 안에 다리를 건너려면 다음과 같이 건너야 합니다.

따라서, 모든 트럭이 다리를 지나려면 최소 8초가 걸립니다.

solution 함수의 매개변수로 다리 길이 bridge_length, 다리가 견딜 수 있는 무게 weight,
트럭별 무게 truck_weights가 주어집니다.
이때 모든 트럭이 다리를 건너려면 최소 몇 초가 걸리는지 return 하도록 solution 함수를 완성하세요.
'''

# 제한 조건
'''
bridge_length는 1 이상 10,000 이하입니다.
weight는 1 이상 10,000 이하입니다.
truck_weights의 길이는 1 이상 10,000 이하입니다.
모든 트럭의 무게는 1 이상 weight 이하입니다.
'''
from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 1
    tmp = truck_weights.pop(0)
    b_weight = tmp 
    queue = deque()
    queue.append(tmp)
    while ( len(truck_weights) != 0 ):
        # queue의 트럭 개수 == 다리 길이 다음
        if ( len(queue) == bridge_length):
            tmp = queue.popleft()
            b_weight -= tmp
        # 다리에 남은 자리가 있는지
        if ( len(queue) < bridge_length ):
            # 무게가 안넘는지     
            if ( b_weight+truck_weights[0] <= weight):
                tmp = truck_weights.pop(0)
                b_weight += tmp
                queue.append(tmp)
            else:
                queue.append(0)
        answer += 1

    # 다리에 남은 트럭 처리
    while ( len(queue) != 0 ):
        if ( answer < bridge_length): # 앞에 길이 더 남은 트럭
            queue.append(0)
        queue.popleft()
        answer += 1        

    return answer

print(solution(2,10,[7,4,5,6]))
print(solution(100,100,[10]))
print(solution(100,100,[10,10,10,10,10,10,10,10,10,10]))