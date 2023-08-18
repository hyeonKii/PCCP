V = int(input())
E = int(input())

#빈 판 만들기
adj = [[0] * (V + 1) for _ in range(V + 1)]

for _ in range(E):
    s, e = map(int, input().split())
    adj[s].append(e)
    adj[e].append(s)

#bfs 돌기

from collections import deque

queue = deque([1])
visited = set([1])

while queue:
    now = queue.popleft()

    for after in adj[now]:
        if after not in visited:
            queue.append(after)
            visited.add(after)

print(len(visited) - 2)