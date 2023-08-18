V = int(input())
E = int(input())

#빈 판 만들기
adj = [[0] * (V + 1) for _ in range(V + 1)]

for _ in range(E):
    s, e = map(int, input().split())
    adj[s][e] = 1
    adj[e][s] = 1

#dfs 돌기
from collections import deque

stack = deque([1])
visited = set([1])

while stack:
    now = stack.pop()

    for after in range(V + 1):
        if adj[now][after] == 1 and after not in visited:
            stack.append(after)
            visited.add(after)

print(len(visited) - 1)