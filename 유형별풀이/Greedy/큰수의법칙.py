# Greedy - 큰수의 법칙
# 주어진 수를 M번 더하여 가장 큰 수를 만드는 법칙, 특정한 숫자가 연속으로 K번을 초과하여 더해질 수 없음

#  첫째줄에 2 <= N <= 1000, 1 <= M <= 10000, 1 <= K <= 10000의 자연수, 자연수는 공백 구분
# 둘째 줄에 N개의 자연수가 주어지며, 자연수는 공백 구분, 각 자연수는 M의 조건에 만족함
#

import sys

def make_big_nums(var, nums):
    answer = 0

    N = var[0] # 입력 숫자 개수
    M = var[1] # 더해야하는 횟수
    K = var[2] # 횟수 제한

    nums.sort(reverse=True) # 내림차순 정렬

    # 가장 큰수 K번 반복 + 그 다음 수 1번 반복 = (K+1)
    n1 = int(M/(K+1))*K
    n1 += M%(K+1) # 수열이 K+1로 나눠떨어지지 않을 때
    answer = nums[0]*n1 + nums[1]*(M-n1)
    
    return answer

if __name__ == '__main__':
    var = list(map(int,sys.stdin.readline().rstrip().split(" ")))
    nums = list(map(int,sys.stdin.readline().rstrip().split(" ")))
    print(make_big_nums(var,nums))