## 탐색

- [완전 탐색](#완전-탐색)(Exaustive Search)
- [탐욕 알고리즘](#탐욕-알고리즘)(Greedy)
- [순차 탐색](#순차-탐색)(Sequential Search)
- [이진 탐색](#이진-탐색)(Binary Search)

---

#### 완전 탐색

- 모든 경우의 수를 탐색
- Brute-force, generate-and-test

#

#### 탐욕 알고리즘

- **최적해**를 구하는 데 사용되는 **근시안적**인 방법
- 그 순간의 최적이라고 생각되는 것을 선택해 나가는 방식
- 일반적으로 머릿속으로 반복의 끝 지점이나 예상을 하기 힘들 때 접근하는 방법

#

#### 순차 탐색

- **정렬되어 있지 않은 경우**

  - 순서와 상관없이 빨리 찾을 수도 있지만 찾지 못하면 무조건 끝까지 탐색해야함.

  ```python
  def sequential_search(list, target):
  	for i in range(len(list)):
  		if list[i] == target:
  			return i
  	else:
  		return -1
  ```

- **정렬되어 있는 경우**
  - 순서대로 정렬 돼 있으므로 원하는 타겟의 크기를 초과할 경우 빠르게 실패를 반환할 수 있으나 우연히 빨리 찾지는 못 함.
  ```python
  def sequential_search(list, target):
  	for i in range(len(list)):
  		if list[i] == target:
  			return i
  		elif target < list[i]:
  			return -1
  	else:
  		return -1
  ```

#

#### 이진 탐색

- 순서대로 정렬 돼 있을 때 가능.
- 자료의 가운데서부터 값을 비교하며 해당하는 범위에서 다시 반복

```python
def binary_search(list, target):
	start = 0
	end = len(list) - 1
	while start <= end :
		middle = (start + end) // 2
		if list[middle] == target:
			return middle
		elif list[middle] > target:
			end = middle - 1
		else:
			start = middle + 1
	return -1
```
