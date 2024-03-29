# Class와 Method

---

Python에서 method란 클래스 안에서 선언된 함수를 말한다.

Method는 영향을 주는 범위에 따라 3가지로 나뉜다.

- **CLASS method** : 클래스 자체에 영향을 주고 선언시 인자로 cls(class)를 포함한다. _@classmethod_ (데코레이터) 를 상위에 명시해야 한다.

- **INSTANCE method** : 생성될 인스턴스에 영향을 주고 인자로 self(생성시 인스턴스)를 포함한다.

  - 생성자 메서드: 객체가 생성될 때 필요한 속성을 할당시키며 생성할 수 있게 해주는 메서드, 객체가 생성될 때 자동으로 실행

  ```python
  class Person:
      def __init__(self, name, age):
          # 생성될 객체에 name과 age를 인자로 받아서
          # 객체의 속성으로 할당
          self.name = name
          self.age = age
  p1 = Person("song", 24)
  ```

  - 소멸자 메서드: 객체가 삭제될 때 호출되는 메서드

  ```python
  class Person:
    def __del__(self):
        print("삭제")

  del p1
  ```

  - 추가 특별 메서드:
    - `__name__` : 함수의 이름을 대조해주는 메서드
    ```python
    # __main__은 해당 파일 자신을 의미하고
    # 아래의 의미는 자신의 파일에서 실행될 때 참이 되는 조건이다.
    # 즉, 다른 파일에서 import 됐을 때는 아래 문장이 실행되지 않는다.
    if __name__ == "__main__":
        # something...
    ```

- **STATIC method** : 직접적으로는 영향을 주지 않고 인자로 cls와 self를 포함하면 안 된다. 선언 시 _@staticmethod_ (데코레이터) 를 상위에 명시해야 한다.

---

- 간단히 말해 스태틱 메소드는 다른 메소드를 도와주기 위한 역할 정도로 생각하면 된다. 보통은 다른 메서드에서 호출하여 쓰는 경우가 일반적이다.

- 생성된 객체(인스턴스)는 클래스, 정적의 입장에서는 알 수가 없다. 각 객체마다 매번 새로운 self를 할당(\_\_init\_\_)) 해주고 인스턴스 객체의 인수인 self로만 접근이 가능하다. 따라서 인스턴스 메서드끼리만 서로의 메서드나 변수 공유가 가능하다.

- 반대로 클래스 메서드나 변수, 정적 메서드 자체는 다른 메서드에서 호출이 가능하다. 단, 꼭 **필요한 경우**에만 사용해야한다.
  - 인스턴스 메서드에서 클래스 변수와 인스턴스 변수를 함께 연산해야할 때
  - 클래스, 인스턴스 메서드에서 특정 기능을 하는 함수(정적 메서드)를 필요로 할 때
- **필요하지 않은 경우(+ 불가능한 경우)**

  - 인스턴스 메서드에서 클래스 변수만 사용하는 경우
  - 정적 메서드에서 다른 종류의 메서드를 호출, 참조
  - 클래스 메서드에서 인스턴스 메서드를 참조 (클래스 입장에서는 각 객체(인스턴스)를 모르기 때문에 접근할 수 없음)

- 같은 클래스 안에서의 선언은 순서를 따지지 않는다. (아직 선언되지 않은 메서드를 다른 메서드에서 호출 가능하다. 실제 실행이 아니기 때문에 인터프리터는 그냥 참고만 하기 떄문)

---

```python
class Person:
    total_person = 0

    def count_total_person(cls): # class-method
        cls.total_person += 1

    def talk(self, content): # instance-method
        self.content = content

    @staticmethod
    def meet(person):  # static-method
        print(f"Hello, {person}")
```

위의 형식중 **@something**은 **데코레이터**라는 문법으로 함수의 선언 위에 쓰여, 그 함수가 나중에 실행 될 때, 특정 기능을 추가해준다.

```python
def deco(func):                             # 호출할 함수를 매개변수로 받음
    def wrapper():                           # 호출할 함수를 감싸는 함수
        print(func.__name__, '함수 시작')    # __name__으로 함수 이름 출력
        func()                               # 매개변수로 받은 함수를 호출
        print(func.__name__, '함수 끝')
    return wrapper                           # wrapper 함수 반환
    .
    .
    .
@deco
def any_func_name():
    pass                # 이후 함수 실행시마다 지정해둔 데코레이터를 실행

```

---

## 상속

클래스를 정의할 때 사용한 메서드들을 이용하여 새로운 클래스를 생성하고 싶은 경우 사용.

```python
# ws_8_4
class PublicTransport:

    def __init__(self, name, fare):
        self.name = name
        self.fare = fare
        self.total_passenger = 0

    def get_in(self, number_of_passenger):
        self.total_passenger += number_of_passenger

    def get_out(self, number_of_passenger):
        self.total_passenger -= number_of_passenger

    def profit(self):
        return self.fare * self.total_passenger


# 인자로 상속 받은 부모 클래스를 작성함
class Bus(PublicTransport):
    # 필요한 부분은 오버라이팅으로 새로 작성
    def __init__(self, name, fare, limit):
        self.name = name
        self.fare = fare
        self.total_passenger = 0
        self.limit = limit

    def get_in(self, number_of_passenger):
        self.total_passenger += number_of_passenger
        if self.total_passenger > self.limit:
            print("더 이상 탑승할 수 없습니다.")


bus = Bus("bus", 500, 20)
bus.get_in(19)
print("====")
bus.get_in(19)

```

- mro 함수
  - 원하는 인스턴스나 클래스 등이 어떤 부모나 조상을 가지는지 보여줌

---

## QnA

Q1. 클래스 선언 시 아래 두개 예시의 차이는?

```
class Person:
    pass
```

```
class Person():
    pass
```

A1. 첫 번째 경우가 일반적이다. 상속을 받을 때 Person이 부모를 인자로 받기도 하는데 위의 경우에는 인자로 받은 부모가 없으므로 "()"는 생략하는 것이 좋다.

---

Q2. 인스턴스 메소드 선언 시 내용에 같은 클래스 안의 스태틱 메소드를 불러오고 싶다면 어떻게 불러와야 하는지

A2.

```python
class Person:

    def talk(self, content):
        self.content = content
        self.revise_content(self.content)
        # 스태틱 메소드도 마찬가지로 인스턴스의 메소드로서 실행됨
        # 물론 class.메소드명 으로 실행해도 가능은 하지만
        # 인스턴스 메소드 안에서는 인스턴스를 객체로 쓰는 것이 원칙
    @staticmethod
    def revise_content(content):
        return content + "something"

```

---

Q3. 클래스 밖에서 따로 스태틱 메소드만 실행 시키고 싶으면?

A3.

```python
p1 = Person()
p1.talk("HI")           # talk를 통해 받은 스태틱 메소드가 실행 됨
p1.revise_content("HI") # p1(인스턴스)가 직접 실행
Person.revise_content("HI") # 클래스를 통해 찾아서 실행
```

---

Q4. 반대로 스태틱 메소드 안에서 인스턴스 메소드를 부르게 되면?

A4. 스태틱 메소드에서 인스턴스 메소드를 부르려면 "self.인스턴스메소드" 형식으로 불러야하는데 스태틱 메소드에서는 인자에 self가 없기 때문에 불가능

---

Q5. (1) 인스턴스 메소드 안에서 클래스 변수 사용 / (2) 클래스 메소드 안에서 인스턴스 변수 사용

A5.

(1) 만약 인스턴스의 메소드가 클래스 변수까지 사용을 해야하는 경우라면 사용해도 되지만 그냥 클래스 변수만 컨트롤 하려고 사용하는 경우는 당연히 클래스 메소드에서 사용해야함

(2) init으로 생성한 인스턴스 변수들은 다른 인스턴스 메소드에서는 사용 가능하지만 클래스 메소드는 인스턴스 생성을 모르기 때문에 접근이 불가능함

+) 추가로 인스턴스 함수에서 선언된 인스턴스 변수들은 다른 인스턴스 함수에서 접근이 불가능함 (함수의 생명주기), init함수는 "생성자"라는 새로운 개념이라 객체의 요소를 생성함으로써 다른 인스턴스 함수에서는 접근이 가능
