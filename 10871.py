N, X = input().split(' ')
N, X = int(N), int(X)

A = list(map(int,input().split(' ')))

for i in range(N):
    if A[i] < X:
        print(A[i], end = ' ') # 끝에 공백으로 구분하여 출력