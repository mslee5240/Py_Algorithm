n = int(input())    # N 입력받기
plans = input().split()     # 문자열로 입력받기

x, y = 1, 1 # 시작 좌표 설정

# L, R, U, D에 따른 이동 방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

# 이동 계획을 하나씩 확인
for plan in plans:
    # 이동 후 좌표 구하기
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    # 공간을 벗어나는 경우 무시
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue    # for문의 다음 반복으로
    # 이동 수행
    x, y = nx, ny

print(x, y)