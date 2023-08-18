#bfs - 델타

# 입력 세팅(deque, delta, queue)
from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

C, R = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(R)]

queue = deque()

# 2중 for 문으로 초기점 탐색(큐에 추가)

for r in range(R):
    for c in range(C):
        if box[r][c] == 1:
            queue.append((r, c))

#bfs 돌기
    # 큐에 요소들이 존재하지 않을 때까지 1개씩 꺼낸다
while queue:
    # 4방 탐색
    r, c = queue.popleft()
    
    for d in range(4):
        nr, nc = r + dr[d], c + dc[d]
    # 조건을 만족하면 (범위조건, 0인지 확인)
        if 0 <= nr < R and 0 <= nc < C and box[nr][nc] == 0:
    #원본 배열을 변형하고 다음 좌표 큐에 넣을 것
            box[nr][nc] = box[r][c] + 1
            queue.append((nr, nc))


ans = 0
# 정답 판별
    # 배열을 다시 돌면서 0 있는지 확인
for row in box:
    if row.count(0) > 0:
        ans = 0
        break
    # 있으면 -1
    ans = max(ans, max(row))
    # 없으면 배열의 최댓값 -1

print(ans - 1)