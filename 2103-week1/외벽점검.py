'''
    구현 14 외벽점검 - xx

    2020 카카오 신입 공채 1차

    레스토랑의 구조는 완전히 동그란 모양이고, 외벽의 총 둘레는 n 미터이며,
    외벽의 몇몇 지점은 취약한 지점들이 있습니다. 다만 점검은 1시간으로 제한됩니다.
    
    점검을 하는 친구들이 1시간동안 이동할 수 있는 거리는 제각각입니다.
    최소한의 친구들을 투입해 점검하고 나머지는 내부 공사를 돕습니다.

    편의상 정북 방향지점을 0, 취약 지점의 위치는 정북 방향 지점으로부터 시계방향으로 떨어진 거리로 나타냅니다.
    친구들은 출발 지점부터 시계 혹은 반시계 방향으로 외벽을 따라 이동합니다.

    외벽의 길이 n, 취약 지점 위치 배열 weak, 각 친구가 1시간동안 이동할 수 있는 거리가 담긴 배열 dist

    취약 지점을 점검하기 위해 보내야 하는 친구 수의 최솟 값을 return 하세요.
'''
import itertools
 
length = 0
 
def fix(weak, dist):
    index = 0
    size = len(weak)
 
    # 친구들
    for d in dist:
        # 시작점에서 내가 갈 수 있는 한계
        val = weak[index] + d
        for a in range(index, size): # index는 시작점
            if weak[a] <= val: # 위치가 한계를 넘지 않으면
                index = a + 1 # 다음 점으로 이동
            else:
                break # 한계를 넘었으므로 다음 친구에게 넘김
        if index == size: # 모두 고쳤다
            return True
 
    return False
 
def check(weak, dist):
    # 한칸씩 밀어주면서 시작점 변경 - 시작점의 개수가 경우의 수
    for i in range(len(weak)):
        tmp = [weak[a] + length for a in range(i)]
        if fix(weak[i:] + tmp, dist):
            return True
    return False
 
def solution(n, weak, dist):
    global length
    length = n
    dist.sort(reverse=True)
 
    for i in range(1, len(dist) + 1):
        # m명의 친구를 보내는 조합 ( 1~ len(dist)까지)
        perms = itertools.permutations(dist, i)
        for perm in perms:
            if check(weak, perm):
                return i
 
    return -1