## Realized python syntax

---

- set(a) & set(b)

  - set의 교집합 기능을 이용하여 a와 b의 겹치는 부분을 구할 수 있음

  #

- 10 < number < 50

  - 수 비교 연산자도 연달아서 사용 가능

  #

- 삼항연산자

  - var1 = "true_num" if num % 2 == 0 else "false_num")

  #

- List comprehension

  - list1 = [표현식 for 변수 in iterable]
  - dict1 = {key: value for 변수 in iterable}

  #

- for - else 문

  - 반복문이 break로 끝난게 아닐 때 else로 수행하는 문법

  ```
  result = 0
  for i in range(10):
  	if i == 10:
  		result = -1
  		break
  else:
  	result = 1 # 결과는 break에 걸리지 않았으므로 result = 1
  ```

  #

- pass vs continue

  - pass: 없는거나 마찬가지, 다른 코드랑 섞여도 pass는 아무의미 없음
  - continue: 같은 생명주기의 다음 코드들은 생략하고 다음 반복문의 순서로 이동

  #

- 매개변수의 기본값 설정

  ```
  def func(arg1 = 1):
    return arg1

  func(5) # 5
  func() # 1
  ```

  #

- map(<함수>, iterable)

  - iterable을 반복하며 함수를 적용시켜줌

  #

- <iterable>.sort(<key=함수>, reverse=<boolean>)

  - iterable한 데이터를 함수에 반환값을 기준으로 정렬해줌

  #

- if vs except

  - 예상 가능하면 if로 예상 조건에 따라 분류를 해주고
  - 불규칙한, 어디서 에러가 나올지 예상이 안 된다면 except로 예외처리
  - 일반적으로는 if가 속도가 더 빠르고 코드를 볼 때 예상이 가능함

  #

- positional arguments와 keyword arguments

  ```python
  def talk(*content, **person)
    print(content, "This is positional arguments") # list 또는 tuple 형태로 반환
    for key, value in person.items():
      print(f"{key}: {value} "This is keyword arguments"") # dictionary 형태로 반환

  talk("brrrr", name="song", age=24)
  ```

  - keyword argument는 생략가능하기 때문에 positional argument보다 앞에 올 수 없음

  #

- 파이썬에서는 오버라이팅은 있지만 **언패킹(Asterisk)**라는 문법이 있어서 **오버로딩**은 없다.
  - 오버로딩(Overloading) : 같은 이름의 메서드 여러개를 가지면서 매개변수의 유형과 개수가 다르도록 하는 기술
  - 오버라이딩(Overriding) : 상위 클래스가 가지고 있는 메서드를 하위 클래스가 재정의해서 사용

#

- 반복문 사용시 "**\_**"를 사용하면 변수 선언 없이 단순 반복만 할 수 있다.
- 내부에 다시 "**\_**"를 선언해도 오류를 발생시키지 않는다.
- "**\_**" 자체로 빈 공간이라는 의미.

```python
for _ in range(5):
  print("Hello")
```
