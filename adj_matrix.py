Vertex, Edge = map(int, input().split())

adj_list = [[0] * (Vertex + 1) for _ in range(Vertex + 1)]

for _ in range(Edge):
    start, end = map(int, input().split())
    adj_list[start][end] = 1
    adj_list[end][start] = 1

print(adj_list)


# Vertex = 7개, Edge = 8개인 그래프가 있을 때,
# 다음 8개의 줄에 연결 정보를 제공

# 7 8  
# 1 2  
# 1 3
# 2 4
# 2 5
# 4 6
# 5 6
# 6 7
# 3 7