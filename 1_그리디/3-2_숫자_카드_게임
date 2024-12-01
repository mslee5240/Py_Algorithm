# 2중 반복문 구조 이용
n, m = map(int, input().split())

result = 0

for i in range(n):
    data = list(map(int, input().split()))
    # 현재 줄에서 '가장 작은 수' 찾기
    min_value = 10001
    for j in data:
        min_value = min(min_value, j)
    # '가장 작은 수'들 중에서 가장 큰 수 찾기
    result = max(result, min_value)

    print(result)

# # 입력 예시 1
# 3 3
# 3 1 2
# 4 1 4
# 2 2 2

# # 출력 예시 1
# 2