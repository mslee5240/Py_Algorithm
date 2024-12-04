# 보텀업(Bottom-Up): 작은 문제부터 차근차근 답을 도출한다

# DP 테이블 초기화
d = [0] * 100

d[1] = 1
d[2] = 1
n = 99

# 보텀업 DP 구현 - 반복문
for i in range(3, n + 1):
    d[i] = d[i - 1] + d[i - 2]

print(d[n])