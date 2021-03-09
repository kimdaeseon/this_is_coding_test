# 이것이 취업을 위한 코딩테스트다 (저자 나동빈)
# 구현, 왕실의 나이트
# 115p, ch4-3.py

lines = [0,'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

mx = [2,2,-2,-2,1,1,-1,-1]
my = [1,-1,1,-1,2,-2,2,-2]

rx = 0
ry = 0

result = 0

position = input()
x = lines.index(position[0])
y = int(position[1])

for i in range(0,8):
    rx = x + mx[i]
    ry = y + my[i]

    if rx > 8 or rx < 1:
        continue
    if ry > 8 or ry < 1:
        continue
    result += 1

print(result)
