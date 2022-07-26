## SHALLOW COPY and DEEP COPY
---
## 데이터 분류
**데이터의 분류**에 따라 복사가 달라집니다.
데이터는 크게 변경 가능한 것(`mutable`)들과 변경 불가능한 것(`immutable`)으로 나뉘며, python은 각각을 다르게 다룹니다. 먼저 변경 불가능한 데이터를 살펴보겠습니다.


### 변경 불가능한(`immutable`) 데이터
* 리터럴(literal)

    - 숫자(Number)
    - 글자(String)
    - 참/거짓(Bool)

- `range()`
- `tuple()`
- `frozenset()`


### 변경 가능한(`mutable`) 데이터

- `list`
- `dict`
- `set`
---

**복사 방법**

파이썬에서 데이터를 복사하는 방법은 크게, 세 가지로 나뉩니다.
> - 할당 (Assignment)
> - 얕은 복사 (Shallow copy)
> - 깊은 복사 (Deep copy)

https://crackerjacks.tistory.com/14