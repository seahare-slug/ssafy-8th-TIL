# Event

- 네트워크 활동이나 사용자와의 상호작용 등과 같은 동작의 발생

#### event 등록

- **event 처리기**를 통해서 html요소에 **event처리** 활동을 부착해줌
  `targetNode.addEventListener(eventType, listenerFunction)`
- targetNode는 listenerFunction에서 event를 인자로 받아 `event.target`으로 접근 가능

#### event 취소

- 현재 event의 기본 동작을 중단
- HTML에 등록된 기본 동작을 중단
  - `a tag`: 클릭시 특정 주소로 이동
  - `form tag`: form 데이터 전송

```js
const h1 = document.querySelector("h1");
// copy event 등록
h1.addEventListener("copy", function (event) {
  // copy 동작 중단
  event.preventDefalut();
});
```

#

#### lodash

- 모듈성, 성능 및 추가 기능을 제공하는 라이브러리
- 배열, 객체 등 자료구조를 다룰 때 사용
- *https://lodash.com/*
