# 이것이 취업을 위한 코딩테스트다 (저자 나동빈)
# 구현, 시각
# 113p, ch4-2.py

N = int(input())

hour = 0
minute = 0
second = 0
count = 0
while True:
    if hour == N and minute == 59 and second == 59:
        break
    second += 1

    if second >= 60:
        second = 0
        minute += 1
    if minute >= 60:
        minute = 0
        hour += 1
    
    s1, s2 = second%10, second//10
    m1, m2 = minute%10, minute//10
    h1 = hour%10

    if s1 == 3 or s2 == 3 or m1 == 3 or m2 == 3 or h1 == 3:
        count += 1

print (count)