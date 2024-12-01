# BFS(Breadth First Search)
# : 너비 우선 탐색, 가까운 노드부터 탐색하는 알고리즘
# - 동작 원리: 큐
# - 구현 방법: 큐 자료 구조 이용
# - O(N) 시간 소요, DFS보다 빠르다.

# deque([리스트]) => 리스트를 초기 데이터로 전달
# 리스트 형태로 초기 데이터를 전달하면, 리스트의 요소들이 deque 객체에 순서대로 저장된다.

# 리스트, deque, 문자열, 집합, 사전 등의 자료형은
# 비어 있으면 False, 하나 이상의 요소가 있으면 True로 평가됩니다.

from collections import deque   # collections: 모듈 / deque: 클래스

# BFS 메서드 정의
def bfs(graph, start, visited):
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque([start])
    # 현재 노드를 방문 처리
    visited[start] = True
    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력
        v = queue.popleft()
        print(v, end=' ')
        # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

# 각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [6, 8],
    [1, 7]
]

# 각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
visited = [False] * 9

# 정의된 BFS 함수 호출
bfs(graph, 1, visited)
