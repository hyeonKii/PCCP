# 입력받기 setting(delta, input, 케이스)
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

board = [input().split() for _ in range(5)]

cases = set()

# DFS 돌기 (재귀 함수)
    #재귀 함수 (r, c, num)
        
def dfs(r, c, num):
    # len(num) 6 되면 케이스에 넣고 함수 종료
    if len(num) == 6:
        cases.add(num)
        return
    # 4방 탐색
    for d in range(4):
        nr, nc = r + dr[d], c + dc[d]
        # 다음 갈 곳이 보드에 존재하면
        if 0 <= nr < 5 and 0 <= nc < 5:
        # 다음 칸 숫자를 이어붙이고 다음 재귀
            dfs(nr, nc, num + board[nr][nc])
# 2중 for문으로 모든 경우를 돌면서 탐색
for r in range(5):
    for c in range(5):
        dfs(r, c, board[r][c])

#정답은 set 길이
print(len(cases))