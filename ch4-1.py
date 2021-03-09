# 이것이 취업을 위한 코딩테스트다 (저자 나동빈)
# 구현, 상하좌우
# 110p, ch4-1.py

N = int(input())

char = input().split()
length = len(char)
x, y = 1, 1

for i in range(0, length):
    if char[i] == 'U':
        if y <= 1:
            continue
        else: y -= 1
    elif char[i] == 'D':
        if y > N:
            continue
        else: y += 1
    elif char[i] == 'R':
        if x > N:
            continue
        else: x += 1
    elif char[i] == 'L':
        if x <= 1:
            continue
        else: x -= 1

print(x, y)
