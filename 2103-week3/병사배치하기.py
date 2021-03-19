'''
    DP 04 병사 배치하기 백준 18353 - LIS(Longest Increasing Subsequence) 이분탐색 O(NlogN)

    N명의 병사가 무작위로 나열되어 있습니다. 각 병사는 특정한 값의 전투력을 보유하고 있으며, 병사를 배치할 때는
    전투력이 높은 병사가 앞쪽에 오도록 내림차순으로 배치합니다. 다시 말해 앞쪽에 있는 병사의 전투력이 항상 뒤쪽에 있는 병사보다 높아야합니다.
    또한 배치 과정에서 특정한 위치에 있는 병사를 열외시키는 방법을 이용합니다. 그러면서도 남아있는 병사의 수가 최대가 되도록 하고 싶습니다.
'''
import sys

def solution(n,p):
    answer = 0
    q = []
    q.append(p[0])

    # O(N)
    for i in range(1,n):
        if p[i] < q[len(q)-1]:
            q.append(p[i])
        else:
            here = binary_search(q,p[i],0,len(q)-1)
            q[here] = p[i]

    return n-len(q)
        
# O(logN)
def binary_search(array, target, start, end):
    while start < end:
        mid = (start+end) // 2

        if array[mid] == target:
            return mid
        elif array[mid] < target:
            end = mid - 1
        else:
            start = mid + 1
    if start == end:
        return start

if __name__ == '__main__':
    n = int(input())
    p = list(map(int,sys.stdin.readline().rstrip().split(" ")))
    
    print(solution(n,p))