# 이것이 취업을 위한 코딩테스트다 (저자 나동빈)
# DFS/BFS, 음료수 얼려먹기
# 149p, ch5-1.py

from collections import deque

def checkTop(x,y):
    global board

    if x + 1 >= N:
        return False
    
    if board[x + 1][y] == 0:
        return True
    else: return False

def checkBottom(x,y):
    global board

    if x - 1 < 0:
        return False
    
    if board[x - 1][y] == 0:
        return True
    else: return False

def checkLeft(x,y):
    global board

    if y - 1 < 0:
        return False
    
    if board[x][y - 1] == 0:
        return True
    else: return False

def checkRight(x,y):
    global board

    if y + 1 >= M:
        return False
    
    if board[x][y + 1] == 0:
        return True
    else: return False

queue = deque([])

# N 세로길이 M 가로길이
N, M = map(int,input().split())

board = [0] * N

holes = []
visited = []

result = 0

# 0 구멍뚫림, 1 칸막이 있음
for i in range(0,N):
    board[i] = list(map(int, input().split()))

for i in range(0,N):
    for j in range(0,M):
        if board[i][j] == 0:
            holes.append((i, j))


length = len(holes)
while True:
    if length == len(visited): break
    for i in range(0, length):
        if holes[i] not in visited:
            queue.append(holes[i])
            visited.append(holes[i])
            result += 1
            break
    while queue:
        item = queue.popleft()
        i = item[0]
        j = item[1]

        if checkTop(i, j):
            if (i + 1, j) not in visited and board[i + 1][j] != 1:
                queue.append((i + 1, j))
                visited.append((i + 1, j))
        if checkBottom(i, j):
            if (i - 1, j) not in visited and board[i - 1][j] != 1:
                queue.append((i - 1, j))
                visited.append((i - 1, j))
        if checkLeft(i, j):
            if (i, j - 1) not in visited and board[i][j - 1] != 1:
                queue.append((i, j - 1))
                visited.append((i, j - 1))
        if checkRight(i, j):
            if (i, j + 1) not in visited and board[i][j + 1] != 1:
                queue.append((i, j + 1))
                visited.append((i, j + 1))
    

        

print(result)