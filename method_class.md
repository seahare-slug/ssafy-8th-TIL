## Class와 Method
---
Python에서 method란 클래스 안에서 선언된 함수를 말한다.

Method는 영향을 주는 범위에 따라 3가지로 나뉜다.

- __CLASS method__ : 클래스 자체에 영향을 주고 선언시 인자로 cls(class)를 포함한다.

- __INSTANCE method__ : 생성될 인스턴스에 영향을 주고 인자로 self(생성시 인스턴스)를 포함한다.

- __STATIC method__ : 직접적으로는 영향을 주지 않고 인자로 cls와 self를 포함하면 안 된다. 선언 시 *@staticmethod* (데코레이터) 를 상위에 명시해야 한다.
---

간단히 말해 스태틱 메소드는 다른 메소드를 도와주기 위한 역할 정도로 생각하면 된다. 보통은 다른 메서드에서 호출하여 쓰는 경우가 일반적이다.

---
```
class Person:

    def talk(self, content): # instance-method
        self.content = content

    @staticmethod
    def meet(person):  # static-method
        print(f"Hello, {person}")
```
---

## QnA

Q1. 클래스 선언 시 아래 두개 예시의 차이는?
``` 
class Person:
    def ...
```

``` 
class Person():
    def ...
```

A1. 첫 번째 경우가 일반적이다. 상속을 받을 때 Person이 부모를 인자로 받기도 하는데 위의 경우에는 인자로 받은 부모가 없으므로 "()"는 생략하는 것이 좋다.

---

Q2. 인스턴스 메소드 선언 시 내용에 같은 클래스 안의 스태틱 메소드를 불러오고 싶다면 어떻게 불러와야 하는지

A2.
```
class Person:

    def talk(self, content):
        self.content = content
        self.revise_content(self.content)  # 스태틱 메소드도 마찬가지로 인스턴스의 메소드로서 실행됨
                                           # 물론 class.메소드명 으로 실행하도 가능은 하지만 
                                           # 인스턴스 메소드 안에서는 인스턴스를 객체로 쓰는 것이 원칙
    @staticmethod
    def revise_content(content):
        return content + "something"

```
---

Q3. 클래스 밖에서 따로 스태틱 메소드만 실행 시키고 싶으면? 

A3.
```
p1 = Person()
p1.talk("HI")           # talk를 통해 받은 스태틱 메소드가 실행 됨
p1.revise_content("HI") # p1(인스턴스)가 직접 실행
Person.revise_content("HI") # 클래스를 통해 찾아서 실행
```
---
Q4. 반대로 스태틱 메소드 안에서 인스턴스 메소드를 부르게 되면?

A4. 스태틱 메소드에서 인스턴스 메소드를 부르려면 "self.인스턴스메소드" 형식으로 불러야하는데 스태틱 메소드에서는 인자에 self가 없기 때문에 불가능