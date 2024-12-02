# 리스트 컴프리헨션
# [표현식 for 변수 in 반복 가능한 객체 if 조건문]
# - 표현식: 새로 생성될 리스트의 요소를 정의합니다.

# [0] * 3 => [0, 0, 0]

# 입력
n, m = map(int, input().split())    # 맵의 크기 입력받기
x, y, direction = map(int, input().split()) # 현재 캐릭터의 x좌표, y좌표, 방향을 입력받기

# 전체 맵 정보 입력받기
map_info_arr = []
for i in range(n):
    map_info_arr.append(list(map(int, input().split())))

# 방문할 위치를 저장하기 위한 맵을 생성하여 0으로 초기화
visit_arr = [[0] * m for _ in range(n)]

visit_arr[x][y] = 1 # 현재 좌표 방문 처리

# 북, 동, 남, 서 방향 정의
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 왼쪽으로 회전
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

# 시뮬레이션 시작
count = 1
turn_time = 0
while True:
    # 왼쪽으로 회전
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    # 회전한 이후 정면에 가보지 않은 칸이 존재하는 경우 이동
    if visit_arr[nx][ny] == 0 and map_info_arr[nx][ny] == 0:
        visit_arr[nx][ny] = 1   # 방문 처리
        # 이동
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    # 회전한 이후 정면에 가보지 않은 칸이 없거나 바다인 경우
    else:
        turn_time += 1
    # 네 방향 모두 갈 수 없는 경우
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        # 뒤로 갈 수 있다면 이동하기
        if map_info_arr[nx][ny] == 0:
            x = nx
            y = ny
        # 뒤가 바다로 막혀 있는 경우
        else:
            break
        turn_time = 0

print(count)