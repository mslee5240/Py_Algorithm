# 모범 답안
n, k = map(int, input().split())
result = 0

while True:
    # (n == k로 나누어 떨어지는 수)가 될 때까지 1씩 빼기
    target = (n // k) * k
    result += (n - target)
    n = target
    # n이 k보다 작을 때(더 이상 나눌 수 없을 때) 반복문 탈출
    if n < k:
        break
    # k로 나누기
    result += 1
    n //= k

# 마지막으로 남은 수에 대하여 1씩 빼기
result += (n - 1)

## 마지막 연산에서 (n - 1)의 의미
# - n이 1이면, (n - 1) = 0 이므로 더할 필요 없음.
# - n이 2 이상이라면, (n - 1) 번의 1을 빼는 연산이 필요.