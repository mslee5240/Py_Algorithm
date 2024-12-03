# 성적이 낮은 순서로 학생 출력하기(key 활용)
n = int(input())

array = []
for i in range(n):
    input_data = input().split()
    # 이름은 문자열 그대로, 점수는 정수형으로 반환하여 저장
    array.append((input_data[0], int(input_data[1])))

# 키(key)를 이용하여, 점수를 기준으로 정렬
array = sorted(array, key=lambda p: p[1])

for i in array:
    print(i[0], end=' ')

# 입력 예시:
# 3
# 홍길동 95
# 이순신 77
# 유관순 85