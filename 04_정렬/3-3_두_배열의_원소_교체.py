# n개의 원소, 최대 k번의 바꿔치기
n, k = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()    # 배열 A는 오름차순 정렬 수행
b.sort(reverse=True)    # 배열 B는 내림차순 정렬 수행

# 첫 번째 인덱스부터 확인하여, 두 배열의 원소를 최대 K번 비교
for i in range(k):
    if a[i] < b[i]: # A의 원소가 B의 원소보다 작은 경우
        a[i], b[i] = b[i], a[i]
    else:   # A의 원소가 B의 원소보다 크거나 같을 때, 반복문을 탈출
        break

print(sum(a))   # 배열 A의 모든 원소의 합을 출력

# 입력 예시:
# 5 3
# 1 2 5 4 3
# 5 5 6 6 5