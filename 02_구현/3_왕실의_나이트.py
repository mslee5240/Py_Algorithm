# 현재 나이트의 위치 입력받기
input_data = input()

row = int(input_data[1])    # 행
column = int(ord(input_data[0])) - int(ord('a')) + 1   #열

# ord() 함수는 단일 문자(character)를 해당하는 유니코드 값(정수)으로 변환하는 함수. 
# ex) ord('A') == 65

# 나이트가 이동할 수 있는 8가지 방향 정의
steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

# 8가지 방향에 대하여 각 위치로 이동이 가능한지 확인
result = 0
for step in steps:
    # 이동하고자 하는 위치 확인
    next_row = row + step[0]
    next_column = column + step[1]
    # 해당 위치로 이동이 가능하다면 카운트 증가
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_row <= 8:
        result += 1

print(result)