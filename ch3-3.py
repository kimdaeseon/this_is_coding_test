# 이것이 취업을 위한 코딩테스트다 (저자 나동빈)
# 그리디, 1이 될 때 까지
# 92p, ch3-3.py

N, K = map(int, input().split())
count = 0
while True:
    if N % K == 0: N = N // K
    else: N = N - 1
    count = count + 1
    if N == 1: break;

print (count)