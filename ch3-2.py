# 이것이 취업을 위한 코딩테스트다 (저자 나동빈)
# 그리디, 숫자 카드 게임
# 96p, ch3-2.py

N , M = map(int, input().split())

array = [0]*N

for i in range(0, N):
    array[i] = list(map(int, input().split()))

mini = 10001

for i in range(0, N):
    for j in range(0,M):
        if array[i][j] < mini:
            mini = array[i][j]
    array[i].append(mini)
    mini = 10001

max = -1

for i in range(0,N):
    if array[i][M] > max:
        max = array[i][N]

print(max)