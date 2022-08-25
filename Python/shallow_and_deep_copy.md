## SHALLOW COPY and DEEP COPY

---

**복사 방법**

파이썬에서 데이터를 복사하는 방법은 크게, 세 가지로 .

> - 할당 (Assignment)
> - 얕은 복사 (Shallow copy)
> - 깊은 복사 (Deep copy)
>   https://crackerjacks.tistory.com/14

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
