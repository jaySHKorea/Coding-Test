'''
    그래프이론 02 - 탑승구 20m

    공항에는 G개의 탑승구가 있으며, 1번부터 G번까지의 번호로 구분된다.
    공항에는 P개의 비행기가 차례대로 도착할 예정이며, i번째 비행기를 1~G번의 탑승구 중 하나에 영구적으로 도킹해야한다.
    다른 비행기가 도킹하지 않은 탑승구에만 도킹할 수 있다.
    또한 P개의 비행기를 순서대로 도킹하다가 만약에 어떠한 탑승구에도 도킹할 수 없는 비행기가 나오는 경우, 그 시점에서 공항의 운행을 중지한다.
    공항의 관리자는 최대한 많은 비행기를 공항에 도킹해야하는데, 최대 몇대를 도킹할 수 있을까?
'''
import sys

def solution(G,P,docking):
    answer = 0
    dock = [0 for i in range(G+1)]

    # 각 탑승구에 도킹 가능한 비행기 개수 카운트
    for gi in docking:
        for i in range(1,gi+1):
            dock[i] += 1

    # 도킹
    for gi in docking:
        mindock = min(dock[1:gi+1]) # 탑승구에 가능한 비행기 수가 적은 것부터
        if mindock == int(1e9): # 가능한 탑승구가 없다
            break
        idx = dock[1:gi+1].index(mindock)+1
        dock[idx] = int(1e9) # 도킹 완료
        answer += 1

    return answer

if __name__ == '__main__':
    G = int(input())
    P = int(input())

    docking = []

    for i in range(P):
        docking.append(int(input()))
    print(solution(G,P,docking))