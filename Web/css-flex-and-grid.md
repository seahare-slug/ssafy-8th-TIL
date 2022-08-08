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

#

- **정렬**
  - `justify`: main-axis 기준으로 정렬
    - `content`: 한 줄을 하나로 보고 정렬
    - `items`: flex에서는 적용 안 됨. 각 요소의 영역을 기준으로 정렬이지만 각 요소의 영역이 정의되지 않음.
    - `self`: flex에서는 적용 안 됨. 자신의 영역을 기준으로 정렬이지만 자신의 영역이 정의되지 않음.
  - `align`: cross-axis 기준으로 정렬
    - `content`: wrap이 설정된 상태여야 함. 높이에 대한 여백에 있어야함. 한 줄을 하나로 보고 정렬.
    - `items`: 높이에 대한 여백이 있어야함. 각 요소를 기준으로 정렬.
    - `self`: flex에서는 적용 안 됨.

#

- **정렬의 종류**
  - `center`: 가운데 정렬
  - `flex-start`: 기준의 출발점으로 정렬(justify의 기본값)
  - `flex-end`: 기준의 끝점으로 정렬
  - `space-between`: 양 끝 여백은 없애고 나머지 여백을 똑같이. 0 요소 1 요소 1 요소 0
  - `space-around`: 각 요소의 양쪽 여백을 똑같이. 1 요소 1 1 요소 1 1 요소 1.
  - `space-evenly`: 각 요소의 공간을 똑같이. 1 요소 1 요소 1 요소 1.
  - `stretch`: 기준으로 꽉 채워지게(align의 기본값)

# Grid

---

- **선언**

  - 부모(container)에 display: grid로 설정하게 되면 자식들(items)에게 영향을 줄 수 있음.
  - `grid-template-columns: 비율 비율 비율 ...`: 세로축을 기준으로 비율대로 n등분하여 자식들에게 공간을 만들어줌
  - `grid-template-rows: 비율 비율 비율 ...`: 가로축을 기준으로 비율대로 n등분하여 자식들에게 공간을 만들어줌

#

- **정렬**
  - flex와 다르게 자식요소들의 공간을 만들어주기 때문에 items 각각의 공간을 기준으로 정렬이 가능
  - `justify-items`: 자식요소의 공간들의 기준으로 main-axis 정렬.
  - `align-items`: 자식요소의 공간들의 기준으로 cross-axis 정렬. 당연하게도 높이(여분)은 있어야 함
  - `justify-content`: 자식요소 각각의 공간으로 분리 됐기 때문에 불가능
  - `align-content`: 자식요소 각각의 공간으로 분리 됐기 때문에 불가능
  - `justify-self`: 대상 요소에 선언. 선언된 요소에게만 적용.
  - `align-self`: 대상 요소에 선언. 선언된 요소에게만 적용.
