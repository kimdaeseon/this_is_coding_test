# 이것이 취업을 위한 코딩테스트다 (저자 나동빈)
# DFS/BFS, 미로 탈출
# 152p, ch5-2.py

from collections import deque

def checkTop(x,y):
    global board

    if x + 1 >= N:
        return False
    
    if board[x + 1][y] == 1:
        return True
    else: return False

def checkBottom(x,y):
    global board

    if x - 1 < 0:
        return False
    
    if board[x - 1][y] == 1:
        return True
    else: return False

def checkLeft(x,y):
    global board

    if y - 1 < 0:
        return False
    
    if board[x][y - 1] == 1:
        return True
    else: return False

def checkRight(x,y):
    global board

    if y + 1 >= M:
        return False
    
    if board[x][y + 1] == 1:
        return True
    else: return False

# N 세로길이 M 가로길이
N, M = map(int,input().split())

board = [0] * N
resultBoard = [0]*N
queue = deque([])
visited = []
# 0 길있음, 1 괴물 있음
for i in range(0,N):
    board[i] = list(map(int, input().split()))
    resultBoard[i] = [1] * M



queue.append((0, 0))
visited.append((0, 0))
while queue:
    item = queue.popleft()
    i = item[0]
    j = item[1]

    if checkTop(i, j):
        if (i + 1, j) not in visited and board[i + 1][j] != 0:
            queue.append((i + 1, j))
            visited.append((i + 1, j))
            resultBoard[i + 1][j] = resultBoard[i][j] + 1
    if checkBottom(i, j):
        if (i - 1, j) not in visited and board[i - 1][j] != 0:
            queue.append((i - 1, j))
            visited.append((i - 1, j))
            resultBoard[i - 1][j] = resultBoard[i][j] + 1
    if checkLeft(i, j):
        if (i, j - 1) not in visited and board[i][j - 1] != 0:
            queue.append((i, j - 1))
            visited.append((i, j - 1))
            resultBoard[i][j - 1] = resultBoard[i][j] + 1
    if checkRight(i, j):
        if (i, j + 1) not in visited and board[i][j + 1] != 0:
            queue.append((i, j + 1))
            visited.append((i, j + 1))
            resultBoard[i][j + 1] = resultBoard[i][j] + 1

print(resultBoard[N-1][M-1])
print(resultBoard)