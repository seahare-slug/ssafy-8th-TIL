# Flex

- **선언**

  - 부모(container)에 display: flex로 설정하게 되면 자식들(items)에게 영향을 줄 수 있음.

- **axis**

  - main-axis: 정방향 축
  - cross-axis: 정방향과 수직 관계의 축

- **기본값**
  - `flex-direction: row`
  - `flex-basis: auto`
  - `flex-wrap: nowrap`

---

- **`flex-direction`**
  - `row`, `row-reverse`: flex item들이 쌓이는 방향을 행 방향, 행의 역방향으로 설정
  - `column`, `column-reverse`: flex item들이 쌓이는 방향을 열 방향, 열의 역방향으로 설정

#

- **`wrap`**

  - `no-wrap`: flex item이 한 줄에 가득 차게 되면 넘치지 않게 전체적인 item의 width를 작게 조절
  - `wrap`: flex item이 한줄에 가득차게 되면 main-axis의 다음 라인으로 넘겨버림

- **정렬**
  - `justify`:
  - `align`:
    - `content`:
    - `items`:
    - `self`:
      - `center`:
      - `flex-start`:
      - `flex-end`:
      - `space-around`:
      - `space-evenly`:
      - `space-between`:
      - `stretch`:

# Grid

---
