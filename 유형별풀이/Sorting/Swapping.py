'''
    동빈이는 두 개의 배열 A와 B를 가지고 있다. 두 배열은 N개의 원소로 구성되어 있다.
    동빈이는 최대 K번의 바꿔치기 연산을 수행할 수 있는데, A와 B의 원소 하나씩을 교환한다.
    동빈이의 목표는 배열 A의 원소 합이 최대가 되도록 해야한다.
'''

if __name__ == '__main__':
    students = []
    N,K = map(int,input().split())

    A = list(map(int,input().split()))
    B = list(map(int,input().split()))

    A.sort()
    B.sort(reverse=True)

    for i in range(K):
        if ( A[i] < B[i] ):
            A[i],B[i] = B[i],A[i]
        
    print(sum(A))