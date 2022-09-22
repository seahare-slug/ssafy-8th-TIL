# 재귀(Recursion)

- 함수 내부에서 직/간접적으로 자기 자신을 호출하는 함수
- 일반적으로 재귀적 알고리즘은 반복(Iterative) 알고리즘보다 더 많은 메모리와 연산을 필요로 하기 때문에
- 입력 값이 커질수록 재귀는 비 효율적일 수 있다.
- 추상 자료형(list, tree 등)의 구현은 재귀가 간단하고 자연스러운 경우가 많다.

> **2^k^ 연산에 대한 재귀(recursion)와 반복(iteration)**

```python
# Iteration
def Power_of_2(k):
	i = 0
	power = 1
	while i < k:
		power = power * 2
		i = i + 1

	return power
```

```python
# Recursion
def Power_of_2(k):
	if k == 0:
		return 1
	else:
		return 2 * Power_of_2(k - 1)
```

#

> **재귀를 이용한 여러가지 리턴(합) 전달**

```python
number_of_testcase = int(input())

# total을 과정마다 변수로 선언하면 함수 호출시 초기화되거나
# 전역으로 선언해도 과정끼리 같은 전역 total 변수를 참조해버림
# total을 인자로 전달하여 경로에 따른 합을 구할 수 있음
def find_min_route(x, y, total):
    global N
    if x == N and y == N:
        sum.append(total + pad[N][N])
        # 결과를 전역 배열에 저장하면 return 생략가능
        # return
    elif pad[x][y + 1] == 11:
        find_min_route(x + 1, y, total + pad[x][y])
    elif pad[x + 1][y] == 11:
        find_min_route(x, y + 1, total + pad[x][y])
    else:
        find_min_route(x, y + 1, total + pad[x][y])
        find_min_route(x + 1, y, total + pad[x][y])

for test in range(1, number_of_testcase + 1):
    N = int(input())
    pad = [[11] * (N + 2)]
    for i in range(N):
        pad.append([11] + list(map(int, input().split())) + [11])
    total = 0
    sum = []
    pad.append([11] * (N + 2))

    find_min_route(1, 1, total)
    print(f"#{test} {min(sum)}")
```

#

> **선택정렬에 대한 재귀와 반복**

```python
# Iteration
def selection_sort(arr):
    # 0 번 인덱스부터 제일 작은(제일 큰) 원소를 찾아서 채워나가는 방식
    for i in range(len(arr) - 1):
        min_idx = i
        # i 의 다음 위치부터 비교를 하면서 제일 작은 원소의 위치를 찾고, 배열 순회가 끝나면 자리를 바꾼다.
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j  # 최소값 위치 기억
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

```

```python
# Recursion
def selection_sort(arr, i):
    # 재귀적 정의

    # 기저 조건
    if i >= len(arr):
        return
    # 작은 문제의 결과를 통해 큰 문제를 해결하는 유도 조건

    # 현재 위치가 0일때부터 길이 -1 위치를 자리를 찾는다
    # 작은 문제는 현재위치가 i 일때의 그 위치에 맞는 원소를 찾아 자리를 바꾼다.
    min_idx = i  # 최소 원소의 위치를 일단 i 로 시작
    for j in range(i + 1, len(arr)):
        if arr[j] < arr[min_idx]:
            min_idx = j
    arr[i], arr[min_idx] = arr[min_idx], arr[i]
    # ===========================================
    # i 다음 위치로 가서 (i+1) 그 위치에 맞는 최소값을 찾아 바꾸는 일을 한다.
    selection_sort(arr, i + 1)

```
