## SHALLOW COPY and DEEP COPY

---

**복사 방법**

### 얕은 복사 (Shallow copy)

- 대상의 주소를 복사
- immutable한 경우에는 값이 바뀌면 주소도 바뀌기 때문에 복사 대상간의 연관성은 사라지지만
- mutable한 경우에는 값이 바뀌어도 주소가 그대로이기 때문에 복사 대상까지 영향을 줌

**immutable**

```python
# &123[h, e, l, l, o]
a = "hello"
# b가 a의 주소를 참조
b = a
# b의 주소가 새롭게 할당
# &456[y, e, l, l, o]
b[0] = "y"
```

**mutable**

```python
# &123[1,2,3]
a = [1, 2, 3]
# b가 a의 주소를 참조
b = a
# &123[100, 2, 3]
b[0] = 100
# &123[100, 200, 3]
a[1] = 200
```

**활용**

```python
a = 1
arr = [1, 2]
# a -> &123 [1]
# arr -> &1234 [1, 2]

def func1():
	# 지역변수가 아닌 전역변수를 가져옴
	global a
	# a의 주소를 직접 변경
	a += 1
	# a -> &567 [2]

def func2(a):
	# 지역변수 a'를 생성
	# a' -> &123
	# a'가 인자 a의 주소를 참조
	a += 1
	# a' -> &567 [2]
	# 지역변수 a'는 소멸, a는 그대로 %123을 가리킴

def func3(arr):
	# 지역변수 arr'를 생성
	# arr' -> &1234
	# arr'가 인자 arr의 주소를 참조
	arr[0] = 100
	# arr' -> &1234 [100, 2]
	# 배열은 요소의 값이 바뀌어도 주소가 바뀌지 않음
	# 지역변수 arr'이 소멸해도 같은 주소를 참조하고 있는 arr의 요소가 바뀜
```

#

### 깊은 복사 (Deep copy)

- 대상의 객체 자체를 복사, 생성

**copy 모듈의 deepcopy() 사용**

```python
import copy

a = [1, 2, 3]
b = copy.deepcopy(a)
```

**내장된 클래스 안의 copy() 함수 이용**

```python
a = [1, 2, 3]
b = a.copy()
```

**list함수의 매개변수로 원본을 전달**

```python
a = [1, 2, 3]
b = list(a)
```

**슬라이싱**

```python
a = [1, 2, 3]
b = a[:]
```

**반복문을 통한 요소 접근으로의 복사**

```python
a = [1, 2, 3]
b = [ele for ele in a]
```
