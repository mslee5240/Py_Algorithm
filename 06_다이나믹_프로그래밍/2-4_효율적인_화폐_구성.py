n, m = map(int, input().split())
# n개의 화폐 단위 정보를 입력받기ㅣ
array = []
for i in range(n):
    array.append(int(input()))

# DP 테이블 초기화
d = [10001] * (m + 1)

# 보텀업 DP 진행
d[0] = 0
for i in range(n):
    for j in range(array[i], m + 1):
        if d[j - array[i]] != 10001:    # (i - k)원을 만드는 방법이 존재하는 경우
            d[j] = min(d[j], d[j - array[i]] + 1)

# 계산된 결과 출력
print(d[m])

# 입력 예시:
# 3 5
# 3
# 5
# 7
