import sys
from collections import deque
# Baekjoon
# 2667 지렸다 파이썬
# 변수 정의
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
v = []
q = deque()


def bfs(a, b):
    cnt = 1  # 1 갯수
    v[a][b] = 0  # v값이 0이면 방문, 1이면 미방문
    q.append((a, b))

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue

            if v[nx][ny] == 1:
                q.append((nx, ny))
                v[nx][ny] = 0
                cnt += 1
    return cnt


n = int(input())  # 정사각형 길이 받기

for i in range(n): # 맵 받기
    v.append(list(map(int, input())))

count_list = [bfs(i, j) for i in range(n) for j in range(n) if v[i][j] == 1]  # 방문안한 모든 칸에 대해 bfs 돌리고, 횟수 저장

count_list.sort()  # 오름차순 정렬

print(len(count_list))
for i in count_list:
    print(i)


# 5557
# i기 __name__ == '__main__':
#     cnt = 0
#     n = int(input())
#     v = list(map(int, sys.stdin.readline().split()))
#     # dp 배열 선언
#     d = [[0 for _ in range(21)] for _ in range(n)]
#
#     d[0][v[0]] = 1
#     for i in range(1, n-1):
#         for j in range(21):
#             if d[i-1][j]: # 이전 인덱스에서 값이 있을 경우
#                 if 0<=j+v[i]<=20: # 덧셈
#                     d[i][j+v[i]] += d[i-1][j]
#
#                 if 0<=j-v[i]<=20:
#                     d[i][j-v[i]] += d[i-1][j]
#
#     print(d[n-2][v[-1]])



