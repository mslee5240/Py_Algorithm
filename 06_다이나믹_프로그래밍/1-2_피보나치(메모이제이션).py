# 탑다운(Top-Down): 큰 문제를 해결하기 위해 작은 문제를 호출한다.

# 한 번 계산된 결과를 메모이제이션(Memoization)하기 위한 리스틑 초기화
d = [0] * 100

# 탑 다운 DP 구현
def fibo(x):
    # 종료 조건
    if x == 1 or x == 2:
        return 1
    # 이미 계산한 적 있는 문제라면 그대로 반환
    if d[x] != 0:
        return d[x]
    # 아직 계산하지 않은 문제라면 점화식에 따라서 피보나치 결과 반한
    d[x] = fibo(x - 1) + fibo(x - 2)
    return d[x]

print(fibo(99))