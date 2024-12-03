# 퀵 정렬(Quick sort): 기준을 설정한 다음 큰 수와 작은 수를 교환한 후 리스트를 반으로 나누는 방식
# - 왼쪽에서부터 피봇보다 큰 데이터를 찾고, 오른쪽에서부터 피봇보다 작은 데이터를 찾는다.

array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):
    if start >= end:    # 원소가 1개인 경우 종료
        return
    pivot = start   # 피봇은 첫 번째 원소
    left = start + 1
    right = end

    while left <= right:
        # 왼쪽에서부터 피봇보다 큰 데이터를 찾을 때까지 반복
        while left <= end and array[left] <= array[pivot]:
            left += 1
        # 오른쪽에서부터 피봇보다 작은 데이터를 찾을 때까지 반복
        while right > start and array[right] >= array[pivot]:   # 피벗의 위치는 탐색 대상에서 제외
            right -= 1
        
        if left > right:    # 엇갈렸다면 작은 데이터와 피봇을 교체
            array[right], array[pivot] = array[pivot], array[right]
        else:
            array[left], array[right] = array[right], array[left]
    
    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)

quick_sort(array, 0, len(array) - 1)
print(array)

# 조건에서 인덱스 접근 전에 범위 조건을 먼저 확인해야 합니다.
# left <= end and array[left] <= array[pivot] 순서는 범위를 초과하는 인덱스 접근을 방지합니다.
# 반대로 array[left] <= array[pivot] and left <= end 순서로 쓰면 범위를 벗어난 array[left] 접근이 발생해 IndexError를 일으킬 수 있습니다.