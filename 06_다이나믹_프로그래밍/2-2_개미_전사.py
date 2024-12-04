# 보텀업
n = int(input())
# 모든 식량 정보 입력받기
array = list(map(int, input().split()))

# DP 테이블 초기화
d = [0] * 100

# 보텀업 DP 진행
d[0] = array[0]
d[1] = max(array[0], array[1])

for i in range(2, n):
    d[i] = max(d[i - 1], d[i - 2] + array[i])

print(d[n - 1])

# 입력 예시:
# 4
# 1 3 1 5