# 집한(set) 자료형 이용
n = int(input())
# 전체 부품 번호를 입력받아서 집합(set) 자료형에 기록
array = set(map(int, input().split()))

m = int(input())
request = list(map(int, input().split()))

for i in request:
    if i in array:
        print('yes', end=' ')
    else:
        print('no', end=' ')