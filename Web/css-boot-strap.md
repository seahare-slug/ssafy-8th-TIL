# Boot Strap

---

> CDN start
>
> > Include

> > > CSS for
> > > `<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-gH2yIJqKdNHPEq0n4Mqa/HGKIhSkIHeL5AyhkYV8i59U5AR6csBvApHHNl/vI1Bx" crossorigin="anonymous">`

> > > JS for
> > > `<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/js/bootstrap.bundle.min.js" integrity="sha384-A3rJD856KowSb7dwlZdYEkO39Gagi7vIsF0jrRAoQmDKKtQBHUuLZ9AsSv4jD4Xa" crossorigin="anonymous"></script> `

- 장점

  - Boot strap 자체에서 !important로 지정해둔 class를 가져와 바로 사용할 수 있음.
  - 빠른시간에 구현이 가능하고 기본적인 버튼, 레이아웃 등은 바로 가져와 쓸 수 있음.
  - Grid 구현이 쉬움. [How to use](#grid)

  #

- 단점
  - 이미 정해져있는 class를 가져오기 때문에 세밀한 작업은 불가능함.
  - 마찬가지 이유로 색상과 px사이즈등의 조절은 한정적임.

---

#Grid

- Color
  - <span style="color:#007bff">primary</span>
  - <span style="color:#6c757d">secondary</span>
  - <span style="color:#28a745">success</span>
  - <span style="color:#dc3545">danger</span>
  - <span style="color:#ffc107">warning</span>
  - <span style="color:#17a2b8">info</span>
  - <span style="color:#f8f9fa">light</span>
  - <span style="color:#343a40">dark</span>
  - <span style="color:#fff">white</span>

#

- Container
  - container
  - container-fluid

#

- Row / Column
  - row: 한 행에 해당
  - column: 한 열에 해당되며 기본적으로 한 행당 12열로 구성

#

- break-point
  - container, row와 column에 부여할 수 있으며 너비에 따른 공간차지 변화 옵션

```html
<div class="container">
  <div class="row">
    <div class="col-12 col-sm-3">item1</div>
    <div class="row col-12 col-sm-9">
      <div class="col-6 col-sm-6 col-lg-3">item2</div>
      <div class="col-6 col-sm-6 col-lg-3">item3</div>
      <div class="col-6 col-sm-6 col-lg-3">item4</div>
      <div class="col-6 col-sm-6 col-lg-3">item5</div>
    </div>
  </div>
</div>
```

---

# 반응형

- Media Query와 Break Point
  - Media Query
  ```css
  @media (max-width: 1200px) and (min-width: 800px) {
    <!-- 변경하고 싶은 class의 내용 -->
    <!-- 변경되는 범위는 800px ~ 1200px -->
  }
  ```
  - Break Point
  ```html
  col-lg-3
  <!-- 크기가 lg에 해당될 때 col의 차지 공간을 3으로 -->
  ```
