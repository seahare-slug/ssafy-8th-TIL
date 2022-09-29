### 서로소 집합

- 상호배타 집합을 표현하는 방법

  - 연결 리스트
  - 트리

- 상호배타 집합 연산
  - Make-Set(a)
  - Find-Set(a)
  - Union(a, b)

### 최소 신장 트리(MST)

- 그래프에서 최소 비용 문제
  - 두 정점 사이의 최소 비용의 경로 찾기
- #### Prim 알고리즘
  1. 임의의 정점을 하나 선택해서 시작
  2. 선택한 정점과 인접하는 정점들 중에서 최소 비용의 간선을 선택
  3. 모든 정점이 선택될 때 까지 반복
- #### Kruskal 알고리즘
  1. 모든 간선을 가중치에 따라 오름차순 정렬
  2. 가중치가 낮은 간선부터 선택하면서 트리를 증가시킴
  - 사이클이 존재하면 다음으로 낮은 간선 선택
  3. `n-1`개의 간선이 선택될 때까지 2번을 반복
- #### Dijkstra 알고리즘
  - 시작 정점에서 거리가 최소인 정점을 선택해 나가는 방식
  - Prim 알고리즘에 탐욕 기법을 더한 느낌
  - 시작정점(s)부터 끝정점(e)은 최단 경로(s - t) + 최단 경로(t - e)와 같다

```python
# Prim Algorithm

def prim(r, V):
    MST = [0] * (V + 1)  # MST 포함여부
    key = [10000] * (V + 1)  # 가중치를 최대값으로 초기화
    # key[v] => v 가 MST 속한 정점과 연결될 때의 최소 가중치
    key[r] = 0  # 시작점의 key

    for i in range(V):  # 정점중에 선택
        # MST에 포함되지 않은 정점 중에 key 가 최소인 것 찾기
        # MST[i] == 0 ==> MST에 포함되지 않은 정점
        u = 0
        minV = 10000
        for j in range(V + 1):
            if MST[j] == 0 and key[j] < minV:
                u = j
                minV = key[j]
        MST[u] = 1  # 정점 u 를 MST에 추가
        # u 에 인접한 정점들 v 에 대해서 MST 에 포함되지 않은 정점이면
        for v in range(V + 1):
            if MST[v] == 0 and adjM[u][v] > 0:
                key[v] = min(key[v], adjM[u][v])
                # u 를 통해서 MST 에 포함되는 비용과 기존 비용을 비교해서 최소값을 사용
    return sum(key)  # 가중치의 합


V, E = map(int, input().split())
adjM = [[0] * (V + 1) for _ in range(V + 1)]  # 인접 행렬
adjL = [[] for _ in range(V + 1)]  # 인접리스트

for _ in range(E):
    u, v, w = map(int, input().split())
    adjM[u][v] = w
    adjM[v][u] = w  # 가중치가 있는 무방향 그래프,
    adjL[u].append((v, w))
    adjL[v].append((u, w))

print(adjM)
print(adjL)

print(prim(0,V))
```

```python
# Kruskal Algorithm

def find_set(x):
    while x != rep[x]:
        x = rep[x]
    return x


def union(x, y):
    rep[find_set(y)] = find_set(x)


V, E = map(int, input().split())
edge = []
for _ in range(E):
    u, v, w = map(int, input().split())
    edge.append([w, v, u])
edge.sort()
rep = [i for i in range(V + 1)]  # i의 대표는 i

# MST의 간선 개수 = 정점수 - 1
# N 은 정점 수
N = V + 1
# cnt 는 지금까지 선택한 edge 수
cnt = 0
# 가중치의 합
total = 0

# edge를 모두 확인 하면서 하나씩 선택하고,
# 만약 사이클이 생기면 다음거 확인해서 사이클이 안생기는것만 골라서 추가
for w, v, u in edge:
    if find_set(v) != find_set(u):
        cnt += 1
        union(u, v)
        total += w
        if cnt == N - 1:  # MST 구성이 완료되었다.
            break

print(total)
```

```python
# Dijkstra Algorithm

def dijkstra(s, V):
    U = [0] * (V + 1)  # 비용이 결정된 정점을 표시
    U[s] = 1  # 출발점 비용 결정
    for i in range(V + 1):
        D[i] = adjM[s][i]
    # D : 시작점에서 i 번째 정점으로 가는데 걸리는 가중치의 합

    # 정점의 비용 결정
    for _ in range(V + 1):
        # D[정점]가 최소인 w를 결정
        # 아직 비용이 결정되지 않은 정점 중에서 고르면 된다.
        u = 0
        minV = INF
        for i in range(V + 1):
            if U[i] == 0 and minV > D[i]:
                minV = D[i]
                u = i
        U[u] = 1  # 비용을 결정
        for v in range(V + 1):
            if 0 < adjM[u][v] < INF:
                D[v] = min(D[v], D[u] + adjM[u][v])

INF = 10000
V, E = map(int, input().split())
adjM = [[INF]*(V+1) for _ in range(V+1)]

for i in range(V+1):
    adjM[i][i] = 0

for _ in range(E):
    u, v, w = map(int, input().split())
    adjM[u][v] = w

D = [0] * (V+1)
dijkstra(0, V)
print(D)

```
