## 기초 개념

---

- **text-align: center vs margin: 0 auto**

  - text-align: center

    - 대상의 부모에 적용
      - 부모는 block, 자식은 inline일 때
    - 대상에게 바로 적용
      - 대상이 block일 때

  - margin: 0 auto
    - 대상에 적용
    - 부모는 block, 자식의 width는 100%보다 작아야함
    #

- **선택자 우선순위**

  - !important
  - inline style
  - id 선택자
  - class 선택자
  - element(요소) 선택자
  - 소스의 기본 흐름

  #

- **html에 css적용하는 법**

  - inline code
  - style tag
  - 외부 파일

  #

#

- **display: none vs visibility: hidden**
  - display: none
    - 아예 요소 자체를 없애는 것
  - visibility: hidden
    - 요소를 투명하게, 원래 자리는 그대로 차지
  #

#

## 문법

---

- **a(anchor): 닻**

  - href
  - target(\_self, \_blank, \_parent, \_top)
  - rel

  #

- **position**

  - relative: 원래 요소의 자리 차지(O), 옮겨진 위치는 자리 차지(X)
  - absolute: 원래 요소의 자리 차지(X), 옮겨진 위치는 자리 차지(X)
  - fixed: 현재 보이는 스크린에 고정, 스크롤을 해도 그 위치 그대로
  - sticky: 무조건 fixed가 아닌, 스크린의 특정 위치에 닿으면 그 자리에서 fixed

  #

- **display**

  - block: 기본값은 한줄 전체로 width나 height를 지정해 줄 수 있음
    - `<div>, <p>, <form>, <table>`
  - inline: 필요한 최소길이만큼의 width를 차지, 줄바꾸기 없음 width와 height 지정 불가
    - `<span>, <a>, <img>, <button>, <br>, <script>`
  - inline-block: 필요한 최소길이만큼 차지하고 줄바꾸기가 없으나 width와 height를 지정할 수 있음
    - `<button>, <input>, <select>`

  #

- **box-sizing**

  - content-box(기본값): content의 크기를 기준으로 width를 적용
  - border-box: 바깥 테두리까지의 크기를 기준으로 width를 적용

  #

- **:nth-child()**
  - 하위요소 선택자
  - `.some-class > div:nth-child(2)`: some-class의 직계 자식인 div들 중에서 두번째
  - `.some-class div:nth-child(2)`: some-class의 자식, 자손인 div들 중에서 두번째
  - `.some-class :nth-child(2)`: some-class의 자식, 자손인 모든 요소들의 두번째
