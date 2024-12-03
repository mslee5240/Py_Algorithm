# 이진 탐색의 경우 입력 데이터가 많은 문제가 있음
# => sys 라이브러리의 readline() 함수를 이용해서 해결

# 한 줄 입력받아 출력
import sys

# 하나의 문자열 데이터 입력받기
input_data = sys.stdin.readline().rstrip()  # 관행적으로 암기

print(input_data)