# 기초 개념

---

- **p(paragraph): 문단**

#

- **시멘틱 태그**
  - div와 같이 아무 기능은 없지만 가독성, 의미론적 마크업, 검색엔진(SEO)에 영향
  - 만약 필요에 의해서 시멘틱 태그를 `div` 등으로 감싸주게 되어도 SEO는 시멘틱 태그를 먼저 찾은 후 내용으로 판별하기 때문에 기능적으로 상관은 없음. 하지만 관례상 웬만하면 시멘틱 태그를 젤 바깥쪽에 사용함.
  - `<header>`, `<aside>`, `<section>`, `<footer>`

# 문법

---

- **`<form>`**

  - 속성

    - action
    - method
      - GET
      - POST
    - enctype

  - label
  - input

  #

- **목록 태그**
  - `<ol>`: ordered list, 숫자나 알파벳 등 순서가 있는 목록
  - `<ul>`: unordered list, 순서가 필요 없는 목록
  - `<dl>`: definition list, 사전처럼 용어를 설명하는 목록
  - `<li>`: 목록을 나열할 때 사용하는 태그

#

- **`<img/>`** 와 **css: background-img**
  - `<img/>`: html에서 하나의 공간을 차지하는 이미지
  - background-img: 어떤 요소의 배경을 설정해주는 css의 속성으로 공간 차지를 하지 않음
