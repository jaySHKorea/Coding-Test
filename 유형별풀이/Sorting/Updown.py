'''
    위에서 아래로
    하나의 수열에는 다양한 수가 존재한다. 이러한 수는 크기에 상관없이 나열되어 있고, 이 수를 큰 수 부터 작은 수의 순서로 정렬하시오.
'''

if __name__ == '__main__':
    num = []
    N = int(input())
    for i in range(N):
        num.append(int(input()))
    num.sort(reverse=True)
    for i in num:
        print(i, end=' ')