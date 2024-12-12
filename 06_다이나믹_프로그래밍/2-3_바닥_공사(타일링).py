n = int(input())

# DP 테이블 초기화
d = [0] * 1001

# 보텀업 DP 진행
d[1] = 1
d[2] = 3
for i in range(3, n + 1):
    d[i] = (d[i - 1]+ 2 * d[i - 2]) % 796796

print(d[n])

# 예시로 이해하기:

# 2 * 3 직사각형을 채우는 방법(n = 3):
# 1.맨 끝에 1 * 2 하나를 세우면, 남는 공간은 2 * 2
# -> 이걸 채우는 방법은 d[2] = 3

# 2. 맨 끝에 2 * 2 타일 하나를 두거나, 1 * 2 타일 2개를 눕히면,
# 남는 공간은 2 * 1.
# -> 이걸 채우는 방법은 d[1] = 1, 그리고 총 2가지 방법이 있어.
# 결과적으로:
# d[3] = d[2] + 2 * d[1] = 3 + 2 * 1 = 5
