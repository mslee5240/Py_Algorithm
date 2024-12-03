# range의 세 번째 매개 변수
# range의 매개 변수는 3개(start, end, step)이다. 
# 세 번째 매개 변수인 step에 -1이 들어가면 
# start 인덱스부터 시작해서 end + 1 인덱스까지 1씩 감소한다.

for i in range(10, 0, -1):
    print(i, end=' ')