## 정렬

##### 2개 이상의 자료를 특정 기준으로 작은 값부터 큰 값, 또는 큰 값부터 작은 값으로 재배열 하는 것

---

- **대표적인 정렬 방식의 종류**
  - [버블 정렬](#1-버블-정렬)(Bubble Sort)
  - [카운팅 정렬](#2-카운팅-정렬)(Counting Sort)
  - [선택 정렬](#3-선택-정렬)(Selection Sort)
  - 퀵 정렬(Quick Sort)
  - 삽입 정렬(Insertion Sort)
  - 병합 정렬(Merge Sort)

---

### 1. 버블 정렬

- 인접한 두개의 원소를 비교하며 맨 마지막자리까지 이동
- 한 번의 반복에 맨 뒤에서부터 한자리씩 정렬
- O(n^2^)

```python
def bubble_sort(list, N)): # N = len(list)
	for i in range(N - 1, 0, -1): # 맨 뒤부터 정렬된 부분 제외하고 반복
		for j in range(0, i): # 정렬
			if list[j] > list[j + 1]:
				list[j], list[j + 1] = list[j + 1], list[j]
```

### 2. 카운팅 정렬

- 각 항목이 몇 개씩 있는지 세어 개수대로 리스트에 정렬하는 방법
- 리스트 공간을 미리 할당해 놓으려면 정수 값들의 최대값을 알아야 한다
- O(n + k) # n은 리스트의 길이, k는 최대값
- n이 비교적 작을 때 사용 가능

```python
def counting_sort(unsorted_list, k):
	sorted_list = [0] * len(unsorted_list) # 정렬된 배열도 초기 배열이랑 길이가 같음
	count_list = [0] * (k + 1) # 값들의 개수를 저장하는 배열. 배열의 값 범위만큼 배열 생성

	for i in range(0, len(unsorted_list)):
		count_list[list[i]] += 1 # 값의 개수에 따라 카운팅

	for i in range(1, len(count_list)):
		count_list[i] += count_list[i - 1] # 인덱스에 겹치지 않고 맞게 넣어주기 위해 앞의 인덱스를 뒤에 인덱스에 더해줌 (숫자들의 자리 범위 정해주기)

	for i in range(len(sorted_list) - 1, -1 , -1):
		count_list[unsorted_list[i]] -= 1
		sorted_list[count_list[unsorted_list[i]]] = unsorted_list[i] # 원본 배열을 순환하면서 나오는 값들을 정해진 자리에 맞게 넣어줌

```

### 3. 선택 정렬

- 데이터들 중에서 가장 작은 값을 직접 찾아서 맨 앞에 위치시키는 것.
- 찾을 때마다 한 칸씩 뒤에 위치시켜 정렬
- O(n^2^)

```python
def selection_sort(list):
	for i in range(len(list) - 1):
		min_idx = i
		for j in range(i + 1, len(list)):
			if list[min_idx] > list[j]:
				min_idx = j
		list[i], list[min_idx] = list[min_idx], list[i]
```
