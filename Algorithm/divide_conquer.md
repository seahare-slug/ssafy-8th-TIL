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

