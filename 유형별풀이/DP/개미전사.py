'''
    개미 전사는 부족한 식량을 충당하고자 메뚜기 마을의 식량 창고를 몰래 공격하려한다.
    식량 창고는 여러개인데, 일직선으로 이어져 있다. 각 식량창고에는 정해진 수의 식량을 저장한다.
    개미 전사는 선택적으로 창고를 약탈하는데, 메뚜기 정찰병들은 일직선 상에 존재하는 식량창고 중에서
    서로 인접한 식량창고가 공격받으면 바로 알아챌 수 있다. 따라서 개미 전사가 정찰병에게 들키지 않고
    약탈하려면 최소한 한 칸 이상 떨어진 식량창고를 약탈해야한다.

    식량창고에 대한 정보가 주어졌을 때, 얻을 수 있는 식량의 최댓값을 구하시오
'''

def antWarrior(x,array):
    dp = [0]*100

    dp[0] = array[0]
    dp[1] = max(array[0],array[1])
    for i in range(2,x):
        # dp[i-1] : i창고를 안턴다, dp[i-2]+array[i] : i창고를 턴다.
        dp[i] = max(dp[i-1],dp[i-2]+array[i])
    
    return dp[x-1]

if __name__ == '__main__':
    x = int(input())
    array = list(map(int, input().split()))
    print(antWarrior(x,array))