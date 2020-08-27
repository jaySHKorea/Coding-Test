# 백준 14890번 문제

'''
크기가 N×N인 지도가 있다. 지도의 각 칸에는 그 곳의 높이가 적혀져 있다. 

오늘은 이 지도에서 지나갈 수 있는 길이 몇 개 있는지 알아보려고 한다.
길이란 한 행 또는 한 열 전부를 나타내며, 한쪽 끝에서 다른쪽 끝까지 지나가는 것이다. 

길을 지나갈 수 있으려면 길에 속한 모든 칸의 높이가 모두 같아야 한다. 또는, 경사로를 놓아서 지나갈 수 있는 길을 만들 수 있다.
경사로는 높이가 항상 1이며, 길이는 L이다. 또, 개수는 매우 많아 부족할 일이 없다.
경사로는 낮은 칸과 높은 칸을 연결하며, 아래와 같은 조건을 만족해야한다.

경사로는 낮은 칸에 놓으며, L개의 연속된 칸에 경사로의 바닥이 모두 접해야 한다.
낮은 칸과 높은 칸의 높이 차이는 1이어야 한다.
경사로를 놓을 낮은 칸의 높이는 모두 같아야 하고, L개의 칸이 연속되어 있어야 한다.
아래와 같은 경우에는 경사로를 놓을 수 없다.

경사로를 놓은 곳에 또 경사로를 놓는 경우
낮은 칸과 높은 칸의 높이 차이가 1이 아닌 경우
낮은 지점의 칸의 높이가 모두 같지 않거나, L개가 연속되지 않은 경우
경사로를 놓다가 범위를 벗어나는 경우
'''

#입력
#첫째 줄에 N (2 ≤ N ≤ 100)과 L (1 ≤ L ≤ N)이 주어진다. 
#둘째 줄부터 N개의 줄에 지도가 주어진다.
#각 칸의 높이는 10보다 작거나 같은 자연수이다.

#출력
#첫째 줄에 지나갈 수 있는 길의 개수를 출력한다.

'''
3  3  3  3  3  3
2  3  3  3  3  3
2  2  2  3  2  3
1  1  1  2  2  2
1  1  1  3  3  1
1  1  2  3  3  2
'''

import sys

def checkEqual1(iterator):
    iterator = iter(iterator)
    try:
        first = next(iterator)
    except StopIteration:
        return True
    return all(first == rest for rest in iterator)

def line_search(N,L,data):
    n_slope = [0]*100
    j = 1
    prev = data[0]
    while (True):
        if ( j == N ): return 1
        now = data[j]
        # 경사가 달라졌을 때
        if ( abs(prev-now) == 1 ):
            # 경사가 높아졌고, 경사 차이가 1이고, 경사로를 뒤로 놓을만큼 공간이 있을 때
            if ( prev < now and j-L >= 0 ):
                if ( checkEqual1(data[j-L:j]) == True and not 1 in n_slope[j-L:j]): # 뒤로 놓을만큼의 공간의 경사로가 동일할 때
                    n_slope[j-L:j] = [1]*L
                    prev = now
                    j += 1
                else:
                    return 0
            # 경사가 낮아졌고, 경사 차이가 1이고, 경사로를 앞으로 놓을만큼 공간이 있을 때
            elif ( prev > now and j+L <= N ):
                if  ( checkEqual1(data[j:j+L]) == True and not 1 in n_slope[j:j+L]):
                    n_slope[j:j+L] = [1]*L
                    j = j+L
                    prev = data[j-1]
                else:
                    return 0
            else:
                return 0
        # 경사가 그대로일때
        elif ( prev == now ):
            prev = now
            j += 1
        else: # 해당되지 않는 경우 out
            return 0

def solution(N,L,slope_map):
    answer = 0
    
    # 가로
    for i in range(0,N): # 가로 한줄에 대한 탐색
       answer += line_search(N,L,slope_map[i])
    
    # 세로
    for i in range(0,N):
        answer += line_search(N,L,[lst[i] for lst in slope_map])     
    
    return answer

if __name__ == '__main__':
    slope_map = []
    var = list(map(int,sys.stdin.readline().rstrip().split(" ")))
    N = var[0]# 배열크키
    L = var[1]# 경사로 길이
    for i in range(0,N):
        slope_map.append(list(map(int,sys.stdin.readline().rstrip().split()))) # 경사로 배열 입력 받기 list(map(int, list_a))
    
    print(solution(N,L,slope_map))