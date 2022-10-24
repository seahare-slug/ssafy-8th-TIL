# this

- 어떠한 object를 가리키는 키워드
- 일반적인 프로그래밍 언어의 `this`와는 다르게 동작(java의 this, python의 self는 인스턴스 자기자신을 가리킴)
- JS에서는 함수가 호출될 때 `this`를 전달받음
- 이때 함수의 호출 방식에 따라 this에 바인딩 되는 객체가 달라짐
- 함수를 선언할 때 this의 객체가 결정되는 것이 아닌 **호출되는 방식에 따라 동적으로 결정**

#### 전역 문맥에서의 this

- 브라우저의 전역 객체인 window를 가리킴
- 전역 객체는 모든 객체의 유일한 최상위 객체를 의미

`console.log(this) // window`

#### 함수 문맥에서의 this

- 함수를 호출한 방법에 의해 결정됨

#

1.  단순 호출

    - 전역 객체로서의 호출
    - 브라우저에서는 window, Node.js에서는 global

    ```js
    const myFunc = function () {
      console.log(this);
    };
    // 브라우저
    myFunc(); // window

    // Node.js
    myFunc(); // global
    ```

#

2.  Method로서의 호출

    - 객체 안의 메서드로 선언
    - 해당 객체가 바인딩
      ```js
      const myObj = {
        data: 1,
        myFunc() {
          console.log(this); // myObj
          console.log(this.data); // 1
        },
      };
      ```

#

3.  Nested (Function 키워드)

    - forEach의 콜백 함수에서의 this가 메서드의 객체가 아닌 전역 객체 window를 가리킴

      ```js
      const myObj = {
        numbers: [1],
        myFunc() {
          console.log(this); // myObj
          this.numbers.forEach(function (number) {
            console.log(number); // 1
            console.log(this); // window
          });
        },
      };

      myObj.myFunc();
      ```

    - 단순 호출 방식으로 사용됐기 때문인데 **화살표함수**를 사용하여 해결 가능

      ```js
      const myObj = {
        numbers: [1],
        myFunc() {
          console.log(this); // myObj
          this.numbers.forEach((number) => {
            console.log(number); // 1
            console.log(this); // myObj
          });
        },
      };

      myObj.myFunc();
      ```

      - 화살표 함수에서 this는 자신을 감싼 정적인 범위
      - 자동으로 한 단계 상위 scope의 컨텐츠를 바인딩

#### Lexical Scope(static scope)

- 함수를 어디서 호출하는지가 아니라 어디에 선언했는지에 따라 결정
- 화살표 함수는 호출 위치에 상관없이 선언 위치에서 상위 스코프를 가리킴
- 따라서 **함수 내의 함수** 상황에서는 화살표 함수를 쓰는 것을 권장

##### 하지만 또 특별하게

- `addEventListener`에서의 콜백 함수는 특별하게 function 키워드여도 `addEventListener`를 호출한 대상(event.target)을 의미함
- 반면 여기서 화살표함수의 경우에는 상위 scope를 지칭하기 때문에 window 객체가 바인딩 됨

```js
const myBtn = document.querySelector("#myBtn");
myBtn.addEventListener("click", function (event) {
  console.log(this); // <button id="myBtn">myBtn</button>
});

myBtn.addEventListener("click", (event) => {
  console.log(this); // window
});
```

- 따라서 **`addEventListener`의 콜백함수**는 function 키워드를 사용하기
