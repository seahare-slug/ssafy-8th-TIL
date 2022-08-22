### 코딩테스트

- 변화하는 것에 대해 규칙 찾기(**점화식** 찾기)
- 탐색, 예외, 조건 등의 **범위 확인**하기
- 문제에 주어진 범위에 따라 **빈 배열**을 먼저 선언할지 말지

### 문제별 해결법

---

1. [소수 구하가](#소수-구하기)
2. [부분 집합](#부분집합의-개수)
3. [2차원 배열](#2차원-배열)

---

#### 소수 구하기

- 1과 자신만을 약수로 가지는 수
- 소수인지 판별하는 범위는 제곱근까지만 확인
  - 약수는 두수의 곱으로 표현됨
  - 제곱근은 같은 두수의 곱
  - 모든 약수 쌍들은 제곱근을 기준으로 앞뒤로 하나씩 약수를 가짐

#

- 에라토스테네스의 체

  - 소수를 구해야하는 범위가 크다면 미리 배열을 만들어놓고 소수가 아닌 수를 제외
  - 구하는 소수의 범위만큼 배열에 첫번째는 False로, 나머지는 True로 초기화
  - 반복문을 통해서 자기 자신을 제외한 배수들의 위치(인덱스)를 False로 바꿔줌

  ```python
  n = 1000000 	# 소수를 구하는 범위
  che = [True] * (n + 1) # 배열 초기화
  che[1] = False 	# 1은 소수에서 제외

  m = int((n + 1) ** (1/2)) # 소수 판별은 제곱근까지
  for i in range(2, m + 1):
    if che[i]:
      for j in range(2 * i, n + 1, i): # 값 자신을 제외한 배수들은 전부 False로 바꿔줌
        che[j] = False
  ```

  #

#### 부분집합의 개수

- 공집합을 포함한 부분집합의 개수, 제외하려면 -1 해주면 됨
- 각 집합의 원소가 있는지 없는지 2가지로 표현 가능
- 원소의 개수가 n개면 **부분집합의 개수는 2^n^개**로 표현 가능
- 2진수로 표현하면 10000... (0의 개수가 n의 수)

```python
1 << n # n의 개수만큼 비트연산
```

#

#### 2차원 배열

- 2차원 배열의 선언
  - 단순 연산자로만 선언하면 1차원 배열이 여러개 복사가 됨(얕은 복사)
    - `([0] * n) * m`
  - 2차원 배열부터는 1차원 배열을 반복문을 통해 여러번 선언 해줘야함
    - `[0] * n for _ in range(m)`
    - `[0 for _ in range(n)] for _ in range(m)]`

#

- 2차원 배열 출력
  - 언패킹을 이용해서 한 줄씩 출력 가능
    - ```python
      for row in pad:
        print(*row)
      ```

#

- 가로, 세로 방향의 탐색
  - 가로 방향 탐색
    - ```python
      for i in range(number_of_row):
        for j in range(number_of_col):
          pad[i][j]
      ```
  - 세로 방향 탐색
    - ```python
        for i in range(number_of_col):
          for j in range(number_of_row):
            pad[j][i]
      ```

#

- 특정 규칙이 있는 배열 탐색

  - 배열을 탐색하는 순서가 단순히 가로 세로 정도가 아닌 규칙이 있을 때
  - `현재위치 [ci, cj], 다음위치 [ni, nj], 위치사이의 규칙 [1, 0, -1, 0]`
  - `다음위치 = 현재위치 + 위치사이의 규칙`
  - 다음위치의 존재 여부도 조건문을 통해 확인할 수 있다.
  - ex) 달팽이 숫자

    ```python
    pad = [[0] * pad_size for _ in range(pad_size)]

    # 규칙 선언
    di = [0, 1 ,0 ,-1]
    dj = [1, 0 ,-1 ,0]
    d_idx = 0

    ci = 0
    cj = 0
    ni = 0
    nj = 0

    for num in range(1, pad_size**2 + 1):
        pad[ci][cj] = num
        # 다음위치 = 현재위치 + 규칙
        ni = ci + di[d_idx]
        nj = cj + dj[d_idx]
        # 다음위치가 범위를 벗어나거나 값을 다 채웠으면 다음규칙 준비
        if ni < 0 or ni >= pad_size or nj < 0 or nj >= pad_size or pad[ni][nj] != 0:
            # 다음규칙으로 업데이트
            d_idx = (d_idx + 1) % len(di)
        # (다음규칙이 바뀌었으면 바뀐 규칙으로) 현재위치를 업데이트
        ci += di[d_idx]
        cj += dj[d_idx]
    ```