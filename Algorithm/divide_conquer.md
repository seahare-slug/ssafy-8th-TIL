# 분할 정복

- 문제를 분할해서 해결하는 기법
  - 분할(Divide): 해결할 문제를 여러 개의 작은 부분으로 나눈다.
  - 정복(Conquer): 나눈 작은 문제를 각각 해결한다.
  - 통합(Combine): 필요시 해결된 해답을 모은다.
- 대표적으로 병합 정렬과 큌 정렬이 있다.

> 반복을 통한 일반적인 거듭 제곱 알고리즘 O(n)

```python
# Iterative
def Power(power, N):
	result = 1
	for _ in range(N):
		result = result * power
	return result
```

> 분할 정복을 통한 거듭 제곱 알고리즘

```python
# Recursive, divide, conquer O(logn)
def Power(power, N):
	if N == 1:
		return power
	if n % 2 == 0:
		temp = Power(power, N // 2)
		return temp * temp
	else:
		temp = Power(power, (N - 1) // 2)
		return temp * temp
```

#

### 병합 정렬

- 여러 개의 정렬된 자료의 집합을 병합하여 한 개의 정렬된 집합으로 만드는 방식
- 분할 정복 알고리즘을 활용하여 자료를 최소 단위까지 나눈 후 정렬하며 결과를 만들어 냄(top-down 방식)
- 시간복잡도 = O(nlogn)

```python
# 분할 과정
# 반반씩 계속하여 분할
def merge_sort(arr):
	if len(arr) == 1:
		return arr
	left = []
	right = []
	middle = len(arr) // 2

	for i in range(middle):
		left.append(arr[i])
	for i in range(middle, len(arr)):
		right.append(arr[i])

	left = merge_sort(left)
	right = merge_sort(right)

	return merge(left, right)
```

```python
# 병합 과정
# 단위끼리 합치면서 젤 앞의 값부터 비교하며
# 작은 값부터 빼내며 새로운 배열에 정렬
def merge(left, right):
	result = []

	while len(left) > 0 or len(right) > 0:
		if len(left) > 0 and len(right) > 0:
			if left[0] <= right[0]:
				result.append(left.pop(0))
			else:
				result.append(right.pop(0))
		elif len(left) > 0:
			result.append(left.pop(0))
		elif len(right) > 0:
			result.append(right.pop(0))

	return result
```

#

### 퀵 정렬

- 병합 정렬은 그냥 여러 부분으로 나누는 반면에 퀵 정렬은 분할할 때, 기준 아이템(pivot item)을 두어 위치시킨다.

```python
def quick_sort(arr, left, right):
	if left < right:
		pivot = find_pivot(arr, left, right)
		quick_sort(arr, left, pivot - 1)
		quick_sort(arr, pivot + 1, right)
```

**pivot을 찾는 방법은 여러가지**

1. Hoare Partition 알고리즘
2. Lomuto Partition 알고리즘
