# 위에서 아래로(내림차순 정렬)
n = int(input())

array = []
for i in range(n):
    array.append(int(input()))

# 파이썬 기본 정렬 라이브러리를 이용하여 정렬 수행
array = sorted(array, reverse=True)

# 정렬이 수행된 결과를 출력
for i in array:
    print(i, end=' ')

# 입력 예시:
# 5
# 1
# 2
# 3
# 4
# 5