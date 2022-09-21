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
