## 데이터 분류

### 변경 불가능한(`immutable`) 데이터

- 리터럴(literal) <-> +) 반복가능한(iterable)
  - 숫자(Number)
  - 글자(String)
  - 참/거짓(Bool)

* `range()`
* `tuple()`
* `frozenset()`

### 변경 가능한(`mutable`) 데이터

- `list`
- `dict`
- `set`

---

변경 불가능한 데이터는 재할당을 하면 새로운 주소에 값을 다시 생성하고,
변경이 가능한 데이터는 재할당을 해도 주소는 그대로이다.

변수를 통해서 할당을 하면 변수가 가리키는 주소가 "mutable"의 유무에 따라 변하거나 변하지 않는다.

```
a = 3
b = a       # 같은 주소를 가리킴
b = 1       # immutable 데이터이기 때문에 값이 바뀌면 주소도 바뀜
            # 결론적으로 a, b가 다른 주소를 가지게 됨
```

```
a = [1, 2, 3]
b = a           # 같은 주소를 가리킴
b[0] = -1       # 리스트는 mutable 데이터이기 떄문에 요소가 바뀌어도 주소는 그대로임
                # 따라서 b의 요소가 바뀌면 같은 주소인 a의 주소도 바뀜
b = [0, 0, 0]   # 새로운 리스트를 할당 받는 것은 새로운 주소에 할당 됨
```

---

##### (함수 + 클래스) < 모듈 < 패키지 < 라이브러리

---

##### 파라미터(매개변수) <-> 아규먼트(인수)

```python
def talk(content, perosn):  # 매개변수
  pass

talk("hello", world)  # 인수
```

---

##### 데이터 비교 연산과 문자열 선언

```python
def comp_str(str1, str2):
    if str1 is str2:
        return (f"{str1} is {str2}")
    elif str1 == str2:
        return (f"{str1} == {str2}")
    else:
        return "not same"

s1 = "abc"
s2 = "abc"
s3 = "def"
s4 = s1
s5 = s1[:2] + "c"
# is 는 주소까지 같은지 비교
# == 는 내용물의 형태만 비교
print(comp_str(s1, s2)) # s1 is s2
print(comp_str(s1, s3)) # not same
print(comp_str(s1, s4)) # s1 is s2
print(comp_str(s1, s5)) # s1 == s2
```

같은 문자열 선언시 메모리 공간 확보를 위해 새로운 메모리로 바인딩하지 않고 같은 문자열의 주소를 참조함.
따라서 s1과 s2는 각각 선언 돼었지만 같은 주소를 가지고 있음

---

##### boolean이 True 값을 가지는 수

- 조건문 안에 들어가는 0을 제외한 나머지 수
- boolean 연산을 한 정수

```python
5 == True # False
not 5 == False # True
not (not  5) == True # True
if 5 :
  print(True)
```
