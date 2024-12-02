# DFS(Depth-Fist Search)
# : 깊이 우선 탐색이라고도 부르며, 그래프에서 깊은 부분을 우선적으로 탐색하는 알고리즘
# - 동작 원리: 스택 / 구현 방법: 재귀 함수 이용 / O(N) 수행 시간

# 각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
graph = [
    [],
    [2, 3, 8],  # 1번 노드
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7],
]

# 각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
visited = [False] * 9

# DFS 메서드 정의
def dfs(graph, start, visited):
    # 현재 노드를 방문 처리
    visited[start] = True
    print(start, end=" ")   # end=" " 꼭 end랑 등호 붙여서 써야됨
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[start]:  # i는 단순히 현재 노드에서 연결된 다음 노드를 나타낼 뿐, 0부터 시작하는 고정된 값이 아님.
        if not visited[i]:
            dfs(graph, i, visited)

# 정의된 DFS 함수 호출
dfs(graph, 1, visited)