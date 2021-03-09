# 이것이 취업을 위한 코딩테스트다 (저자 나동빈)
# 구현, 게임 개발
# 118p, ch4-4.py

sizeX, sizeY = map(int, input().split())


## 플레이어 x, 플레이어 y, 플레이어 방향 (0 : 북, 1 : 동, 2 : 남, 3 : 서)
px, py, pd = map(int, input().split())


## 북 동 남 서
mx = [0,1,0,-1]
my = [-1,0,1,0]

board = [0]* sizeX
count = 0
rx, ry, rd = px,py,pd

## 갈수있는 칸 0, 가본 칸 2, 바다 1
for i in range (0, sizeY):
    board[i] = list(map(int, input().split()))

board[py][px] = 2

while True:
    rd = (rd - 1) % 4
    rx += mx[rd]
    ry += my[rd]

    if rd == pd:
        rd = (rd + 2) % 4
        px += mx[rd]
        py += my[rd]
        rd = pd 
        if px < 0 or px >=sizeX or py < 0 or py >= sizeY or board[py][px] == 1: break
        count += 1
        continue

    if rx < 0 or rx >=sizeX or ry < 0 or ry >= sizeY:
        rx -= mx[rd]
        ry -= my[rd]
        continue

    if board[ry][rx] == 0:
        px, py, pd = rx, ry, rd
        board[ry][rx] = 2
        count += 1
        continue
    else: 
        rx -= mx[rd]
        ry -= my[rd]
        continue



print (count)

