# 이것이 취업을 위한 코딩테스트다 (저자 나동빈)
# 그리디, 큰수의 법칙
# 92p, ch3-1.py

# 배열의 크기 n, 숫자가 더해지는 횟수 m, 최대 반복 횟수 k
n, m, k = map(int , input().split())
data = list(map(int, input().split()))

max1 = -1
max2 = -1

for i in range(0, n):
    if data[i] > max1:
        max2 = max1
        max1 = data[i]

unit = max1 * k + max2
unitSize = k+1

result = (m // unitSize)* unit + (m % unitSize) * max1

print(result)

