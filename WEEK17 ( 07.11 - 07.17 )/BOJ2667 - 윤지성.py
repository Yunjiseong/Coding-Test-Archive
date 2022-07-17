from collections import deque
# Baekjoon
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