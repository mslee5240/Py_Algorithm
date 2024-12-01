# 단순하게 푸는 법

# 입력 받기
n, m, k = map(int, input().split())
data = list(map(int, input().split()))

# 정렬
data.sort()

first = data[n - 1] # 가장 큰 수
second = data[n - 2] # 두 번째로 큰 수

result = 0

while True:
    for i in range(k):  # 가장 큰 수를 K번 더하기
        if m == 0:  # m이 0이라면 for문 탈출
            break
        result += first
        m -= 1  # 더할 때마다 1씩 빼기
    if m == 0:  # m이 0이라면 while문 탈출
        break
    result += second # 두 번째로 큰 수를 한 번 더하기
    m -= 1  # 더할 때마다 1씩 빼기

print(result)