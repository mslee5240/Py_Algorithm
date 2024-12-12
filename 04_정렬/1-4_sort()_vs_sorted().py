# sort() 메서드
# 정렬 대상: **리스트(list)**에서만 사용할 수 있습니다.
# 작동 방식: 원본 리스트를 직접 변경(in-place)합니다.
# 반환값: None을 반환합니다. 즉, 정렬된 결과를 별도로 반환하지 않습니다.

# sorted() 함수
# 정렬 대상: 리스트뿐만 아니라 모든 반복 가능한(iterable) 객체에서 사용 가능합니다. (예: 리스트, 튜플, 문자열, 딕셔너리 등)
# 작동 방식: 원본 데이터를 변경하지 않고, 정렬된 새로운 객체를 반환합니다.
# 반환값: 정렬된 결과를 포함한 새로운 객체를 반환합니다.

# 리스트 정렬 (둘 다 가능)
# sort() 사용
data = [5, 2, 9, 1]
data.sort()  # 원본 수정
print(data)  # 출력: [1, 2, 5, 9]

# sorted() 사용
data = [5, 2, 9, 1]
new_data = sorted(data)  # 새로운 리스트 반환
print(new_data)  # 출력: [1, 2, 5, 9]
print(data)  # 원본 유지: [5, 2, 9, 1]


# 반복 가능한 객체 정렬 (sorted()만 가능)
# 튜플 정렬
tuple_data = (5, 2, 9, 1)
sorted_tuple = sorted(tuple_data)
print(sorted_tuple)  # 출력: [1, 2, 5, 9]

# 문자열 정렬
string_data = "python"
sorted_string = sorted(string_data)
print(sorted_string)  # 출력: ['h', 'n', 'o', 'p', 't', 'y']ss