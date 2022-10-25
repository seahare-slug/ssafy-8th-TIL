# 기초지식

- string을 index로 접근하여 변경하면 오류는 안 뜨지만 값은 변하지 않은 채로 유지

- 함수를 변수에 저장 가능
- 필요한 모양으로 그때 그때 바꿔서 할당 가능

```js
function func1() {
  return () => {
    console.log("hello");
  };
}
const customFunc = func1();
```
