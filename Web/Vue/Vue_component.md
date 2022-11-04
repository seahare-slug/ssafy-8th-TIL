# Component
- UI를 **독립적**이고 **재사용 가능한** 조각들로 나눈 것
- 기능별로 분화된 코드 조각
- 유지보수를 쉽게 해줄 뿐만 아니라 재사용적인 측면에서도 매우 강력한 기능을 제공
- 하나의 컴포넌트를 재사용하여 반복되는 구조를 쉽게 만들 수 있음
- *재사용성, 확장 가능, 캡슐화, 독립적*

### Component in Vue
- 그렇다면 Vue에서 말하는 component란?
	-	이름이 있는 재사용 가능한 Vue instance(`new Vue()`로 만든 인스턴스)
	- 컴포넌트들이 tree 구조를 이루어 하나의 페이지를 만듦
	- root에 해당하는 최상단의 Component가 App.vue
	- App.vue는 index.html과 연결
	- 결론적으로는 index.html 파일 하나만을 rendering (SPA)

#
## SFC(Single File Component)
- 하나의 Vue 파일이 하나의 Vue instance이고 하나의 Component가 되는 것
- Vue instance에서는 HTML, CSS, JS를 한 파일에서 관리
- 한 Vue에 한 기능 단위로 작성

## Vue Component의 구조
- 템플릿(HTML)
	- HTML의 body부분
	- 눈으로 보여지는 요소
	- 다른 컴포넌트를 HTML 요소처럼 추가 가능
- 스크립트(JavaScript)
	- 컴포넌트 정보, 데이터, 메서드 등
	- Vue 인스턴스를 구성하는 대부분이 작성
- 스타일(CSS)
	- CSS가 작성, 컴포넌트의 스타일 담당

**+) 단방향 데이터 흐름**
- 모든 props는 부모에서 자식으로 아래 단방향 바인딩을 형성
- 하위 컴포넌트가 실수로 상위 컴포넌트 상태를 변경하여 앱의 데이터 흐름에 대한 이해를 힘들게 하는 것을 방지
- 상위 컴포넌트를 변경하려고 시도하면 Vue에서 콘솔을 통해 경고함

#
## Component 등록 3단계
```html
<template>
	<div id="app">
		<!-- 3. 보여주기 -->
		<HelloWorld msg="Welcome to Your App"/>
	</div>
</template>

<script>
	// 1. 불러오기
import HelloWorld from "./components/HelloWorld.vue"

export default {
	name: "App",
	components: {
		// 2. 등록하기
		HelloWorld,
	}
}
</script>
```
1. 불러오기
	- `import {instance name} from {location}`
	- `instance name`: 인스턴스 생성시 작성한 이름
	- src폴더 위치를 `@`로 단축하여 사용가능
	- `.vue` 생략가능
		- `import MyComponent from '@/components/MyComponent'`

2. 등록하기
	- Vue 인스턴스에 `component` 객체의 요소로 등록
3. 보여주기
	- template 안에 `<컴포넌트/>` 형식으로 보여주기

#
## 자식 컴포넌트 작성
```html
<!-- MyChild.vue -->
<template>
	<div>
		<h3>This is child component</h3>
	</div>
</template>

<script>
	export default {
		name: "MyChild"
	}
</script>
```

```html
<!-- App.vue -->
<template>
	<div id="app">
		<HelloWorld msg="Welcome to Your App"/>
		<!-- 3. 보여주기 -->
		<MyChild/>
		<MyChild/>
	</div>
</template>

<script>
import HelloWorld from "./components/HelloWorld.vue"
// 1. 불러오기
import MyChild from "@/components/MyChild"

export default {
	name: "App",
	components: {
		HelloWorld,
		// 2. 등록하기
		MyChild,
	}
}
</script>
```


### Data in components
- 웹페이지를 구현하기 위해서는 독립적인 component마다 같은 Data를 공유할 수 있어야함
- 규칙없이 필요한 component들 끼리 데이터를 주고 받으면
	- 데이터의 흐름을 파악하기 힘듦
	- 유지보수 난이도 증가
- 따라서 부모-자식 관계로만 데이터를 주고 받기로

#### Static props & Dynamic props
- 정적인 데이터를 전달할 때는 "static"을 props 명명 때 명시하기도 함
- 동적인 데이터는 변수를 props로 전달하고 `v-bind`, `v-model`을 이용해서 데이터를 동적으로 바인딩, 부모의 데이터가 업데이트되면 자식으로 전달되는 데이터 또한 같이 업데이트 됨

>static
```html
<!-- App.vue -->
<template>
	<div id="app">
		<!-- 여기서 static-props 속성이 하위 component인 HelloWorld로 보내는 props -->
		<HelloWorld static-props="Welcome to Your App"/>
	</div>
</template>
```
```html
<!-- HelloWorld.vue -->
<template>
	<div>
		<h1>{{ staticProps }}</h1>
	</div>
</template>

<script>
export default {
	name: "HelloWorld",
	// 상위에서 전달 받는 props를 type과 함께 명시
	props: {
		staticProps: String
	}
}
</script>
```
#
>dynamic
```html
<!-- App.vue -->
<template>
	<div id="app">
		<!-- my-dynamic을 변수로 하여 데이터를 전달 -->
		<HelloWorld v-bind:my-dynamic="dynamicProps"/>
	</div>
</template>

<script>
export default {
	name: "#app",
	// 함수를 통해 받은 데이터를 `my-dynamic`에 바인딩하여 전달
	// 각각의 vue 인스턴스가 같은 data 객체를 가지고 있으므로
	// return을 통해 새로운 data 객체를 반환하여 사용해야 함
	data: function () {
		return {
			dynamicProps: "some data",
		}
	}
}
```
```html
<!-- HelloWorld.vue -->
<template>
	<div>
		<h1>{{ myDynamic }}</h1>
	</div>
</template>

<script>
export default {
	name: "HelloWorld",
	props: {
		myDynamic: String
	}
}
</script>
```
> 숫자를 props로 전달하기 위한 방법으로는?
```html
<!-- 1 -->
<Component1 num-props="1"/>
<!-- 2 -->
<Component1 v-bind:num-props="1"/>

<!-- 1번은 정적인 문자 "1"을, 2번은 동적인 정수 1을 전달 -->
```


#
### Pass Props (부모 -> 자식)
- 요소의 속성(property)을 사용하여 데이터 전달
- 자식 컴포넌트는 props 옵션을 사용하여 수신하는 props를 명시적으로 선언해야 함
- 부모에서 넘겨주는 props는 `kebab-case`로 넘겨주면 (HTML), 자식에서 받을때는 자동으로 `camelCase`로 변환하여 인식함

```html
<!-- App.vue -->
<template>
	<div id="app">
		<!-- 여기서 msg 속성이 하위 component인 HelloWorld로 보내는 props -->
		<HelloWorld msg="Welcome to Your App"/>
	</div>
</template>
```
```html
<!-- HelloWorld.vue -->
<template>
	<div>
		<h1>{{ msg }}</h1>
	</div>
</template>

<script>
export default {
	name: "HelloWorld",
	// 상위에서 전달 받는 props를 type과 함께 명시
	props: {
		msg: String
	}
}
</script>
```

### Emit Event (자식 -> 부모)
- 부모 컴포넌트에서 자식 컴포넌트로 데이터를 전달할 때는 이벤트를 통해 전달
	- 데이터를 이벤트 리스너의 콜백함수 인자로 전달
	- 상위 컴포넌트는 이벤트를 통해 데이터를 받음

- `$emit`
	- `$emit("event-name")` 형식으로 사용하며 부모 컴포넌트에 event-name이라는 이벤트가 발생했다는 것을 알림
	- `$emit("event-name")`가 실행되면 event-name 이벤트가 발생하는 것

```html
<!-- MyChild.vue -->
<template>
	<div>
		...
		<!-- childToParent 함수 실행 -->
		<button @click="childToParent">클릭!</button>
	</div>
</template>

<script>
export default {
	...
	methods: {
		childToParent: function () {
			// 부모에 선언된 자신에게 child-to-parent라는 이벤트 스스로 발생
			// 두 번째 인자를 통해 해당 이벤트의 호출 함수의 매개변수로 전달 가능
			this.$emit("child-to-parent", "argument")
		}
	}
}
</script>
```

```html
<!-- MyParent.vue -->
<template>
	...
	<!-- 부모에 선언된 자신에게 이벤트를 발생시켜 부모의 함수를 실행 -->
	<MyChild @child-to-parent="parentGetEvent"/>
</template>

<script>
export default {
	...
	methods: {
		parentGetEvent: function (argument) {
			console.log("이벤트는 자식이 발생했지만 그걸 가지고 있던 부모의 함수가 실행")
			// emit의 두 번째 인자를 통해 해당 이벤트의 호출 함수의 매개변수로 전달 가능
			console.log(argument)
		}
	}
}
</script>
```
#
### pass props / emit event convention(style guide)

- **props**
	- 상위 => 하위 흐름에서 상위에서 **HTML 요소**를 통해 내려줌: `kebab-case`
	- 하위에서 요소를 받을 때는 **JavaScript를 통해** 받음: `camelCase`

- **emit**
	- emit 이벤트를 발생시키면 **HTML 요소가 이벤트를 청취**함: `kebab-case`
	- 메서드, 변수명 등은 **JavaScript에서 사용**함: `camelCase`