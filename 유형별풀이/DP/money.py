'''
    N개의 화폐 종류로 M원을 만들어야할 때, 최소 화폐 개수를 구하여라.
'''
def money(N,M,array):
    dp = [10001]*(M+1)
    dp[0] = 0

    for i in range(N): # 화폐 개수만큼
        for j in range(array[i],M+1): #화폐가치부터 만들어야 할 수까지
            dp[j] = min(dp[j],dp[j-array[i]]+1)

    if dp[M] == 10001:
        return -1
    return dp[M]

if __name__ == '__main__':
    N,M = map(int,input().split())
    array = []
    for i in range(N):
        array.append(int(input()))
    print(money(N,M,array))