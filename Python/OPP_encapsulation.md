# 캡슐화

---

- **객채의 내용에 대해 외부로부터의 직접적인 접근을 차단**
- **파이썬에서 암묵적으로 존재하지만, 언어적으로는 존재하지 않음**
- **개발자끼리의 약속이지, 실제적인 은닉화는 아래와 같은 형태로는 불가능하다는 의미**

#

## Public Member

- 클래스에서 언더바 없이 시작하는 메서드나 속성
- 어디서나 호출 가능, 하위 클래스에서 override 허용
- 기본적인 선언

```python
class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age

p1 = Person("song", 24)
## name과 age 모두 접근 가능
print(p1.name)
print(p1.age)
```

#

## Protected Member

- 언더바 1개로 시작하는 메서드나 속성
- **암묵적**규칙에 의해 부모 클래스 내부와 자식 클래스에서만 호출 가능
- 허위 클래스 override 허용

```python
class Person:
	def __init__(self, name, age):
		self._name = name
		self._age = age

	def get_age(self):
		return self._age

p1 = Person("song", 24)
# 함수를 통해서 protect된 변수 age를 반환
p1.get_age()
# 사실 직접 접근해도 확인 가능하지만
# python에서 암묵적으로 활용할 뿐
print(p1._age)
```

#

## Private Member

- 언더바 2개로 시작하는 메서드나 속성
- 해당 클래스 내부에서만 사용 가능
- 하위 클래스 상속 및 호출 불가능 (에러)
- 외부 호출 불가능 (에러)
  +) protect와 다르게 여기서만 에러가 뜨는 이유는 파이썬 인터프리터에서 "\_\_"가 붙으면 "\_클래스이름"을 추가로 앞에 붙여주기 때문
  +) 따라서 "\_클래스이름\_\_변수"로 쓰면 똑같이 접근 가능함

```python
class Person:
	def __init__(self, name):
		self.__name = name

	def get_name(self):
		return self.__name

p1 = Person("song")

# 메서드를 통해서 호출
print(p1.get_name())
# 에러 발생
print(p1.__name)
# "_클래스이름__변수"형태로 접근
print(p1._Person__name)
```
