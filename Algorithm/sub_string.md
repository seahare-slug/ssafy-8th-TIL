### Find sub-string Algorithm

---

- [KMP](#kmp-algorithm)
- [라빈-카프](#)
- [보이어 무어](#)

#

#### KMP Algorithm

---

**target_str의 앞뒤의 일치 패턴을 찾아 불필요한 반복 탐색을 막는 방법**

1. 찾고자하는 부분 문자열(sub-string)에 대해 앞뒤(접두, 접미)의 일치 패턴의 길이를 찾는다.
   - ababbab
     - a -> 0
     - ab -> 0
     - **a**b**a** -> 1
     - **abab** -> 2
     - ababb -> 0
     - **a**babb**a** -> 1
     - **ab**abb**ab** -> 2
2. 전체 문자열에서 탐색하며 일치하지 않는 부분을 찾아 다시 탐색해야할 때 다시 탐색을 시작할 위치를 앞뒤 일치 패턴의 길이를 이용하여 선택

```python
def kmp(total_str, target_str):
	# 일치 패턴의 길이 "pi" 찾기
	pi = [0 for _ in range(len(target_str))]
	i = 0

	for j in range(1, len(target_str)):
		while i > 0 and target_str[i] != target_str[j]:
			i = pi[i - 1]

		if target_str[i] == target_str[j]:
			i += 1
			pi[j] = i

  # 패턴을 이용한 전체 문자열 탐색
	result = []
	i = 0
	for j in range(len(total_str)):
		while i > 0 and target_str[i] != total_str[j]:
			i = pi[i - 1]

		if pi[i] == total_str[j]:
			i += 1
			if i == len(target_str):
				result.append(j - i + 1)
				i = pi[i - 1]

	return result
```

#

#### Rabin-Karp Algorithm

---

**해시 값(제곱수와 해당 값의 곱)을 이용하여 target_str의 해시 값과 total_str에 포함된 문자열의 해시 값을 비교**

1. target_str의 해시 값을 구한다.

   - ABCD -> (ord(A) \* 3^3^) + (ord(B) \* 3^2^) + (ord(C) \* 3^1^) + (ord(D) \* 3^0^)

2. total_str에서 target_str의 길이만큼 순회하면서 해시 값을 계산하고 target_str과 비교한다.

해시 값 = target \* str의 길이 \* (target_str의 해시값 \- 맨 앞의 문자열 값 \* target_str의 길이^제곱수^) \+ 탐색할 total_str의 문자열
