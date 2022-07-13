import sys

if __name__ == '__main__':
<<<<<<< HEAD
    cnt = 0
=======
>>>>>>> def3b82f4b442ec1073e8f7b0ad2407bc4439a19
    n = int(input())
    v = list(map(int, sys.stdin.readline().split()))
    # dp 배열 선언
    d = [[0 for _ in range(21)] for _ in range(n)]

    d[0][v[0]] = 1
    for i in range(1, n-1):
        for j in range(21):
            if d[i-1][j]: # 이전 인덱스에서 값이 있을 경우
                if 0<=j+v[i]<=20: # 덧셈
                    d[i][j+v[i]] += d[i-1][j]

                if 0<=j-v[i]<=20:
                    d[i][j-v[i]] += d[i-1][j]

<<<<<<< HEAD
    print(d[n-2][v[-1]])
=======
    print(d[n-2][v[-1]])
>>>>>>> def3b82f4b442ec1073e8f7b0ad2407bc4439a19
