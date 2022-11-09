# Vue Router
- SPA / CSR 의 환경에서 사용할 예정
- 하나의 HTML 파일만을 제공하고 JavaScript, axios 등을 통해 DOM을 통제
- 하나의 HTML 파일이지만 동작에 따라 URL을 바꾸기 위해 사용 (UI / UX 관점)
- 링크 공유, 뒤로가기 기능 등을 구현 가능

```
// Vue Router 실행

$ vue create vue-router-app

$ cd vue-router-app

// 프로젝트 진행중 router를 추가하면 App.vue가 덮어써지기 때문에 유의
$ vue add router
```

#### History mode 사용여부
- 브라우저의 history API를 이용한 방식
- 새로고침 없이 URL 기록을 남길 수 있음
- history mode를 사용하지 않으면 hash mode가 기본 값임
	- history mode: `http:.../index`
	- hash mode: `http:...#index`

#
## Vue Router 시작하기
- router-link 추가
	- a 태그와 비슷한 기능
	- 목적 경로는 `to`속성으로 지정
	- routes에 등록된 component와 매핑됨
	```html
	<!-- App.vue -->

	<template>
		<div id="app">
			<nav>
				<router-link to="/">Home</router-link>
				<router-link to="/about">About</router-link>
			</nav>
		</div>
	</template>
	```
#
- views 폴더 생성
	- 주어진 URL에 대해 일치하는 component를 렌더링 하는 component
	- 실제 component가 DOM에 부착되어 보이는 자리를 의미
	- Django의 block tag와 비슷함
		- App.vue는 base.html의 역할
		- router-view는 block tag로 감싼 부분
#
- router/index.js 생성
	- router에 관련된 정보 및 설정이 작성되는 곳
	- Django에서 urls.py에 해당
	- router에 URL과 component를 매핑
	```js
	const routes = [
		{
			path: "/",
			name: "home",
			component: HomView
		},
	]
	```
#
## 선언적 방식 네비게이션
- router-link의 `to` 속성으로 주소 전달
- 이름을 가지는 routes
	- Django에서 path 함수의 name 인자의 활용과 같은 방식
		```js
		// router/index.js

		const routes = [
			{
				path: "/",
				name: "home",
				component: HomeView
			},
		]
		```
	- 동적인 값을 사용하기 때문에 v-bind를 사용해야 정상적으로 작동
		```html
		<!-- App.vue -->
		...,
		<router-link :to="{ name: 'home' }">Home</router-link>
		<router-link :to="{ name: 'about' }">About</router-link>
		```
#
## 프로그래밍 방식 네비게이션
- vue 인스턴스 내부에서 라우터 인스턴스에 `$router`로 접근 할 수 있음
- 다른 URL로 이동하려면 `this.$router.push`를 사용
	- history stack에 이동할 URL을 넣는 방식
	- 기록이 남기 때문에 뒤로가기 등의 기능 사용 가능
- 동작 원리는 선언적 방식과 같음
	```html
	<!-- somethingView.vue -->
	<template>
		<button @click="toHome">홈으로</button>
	</template>

	<script>
	export default {
		...,
		methods: {
			toHome() {
				this.$router.push({ name: "home" })
			}
		}
	}
	</script>
	```
#
## Dynamic Route Matching
- 동적인 라우트 활성화
1. View component 작성
	```html
	<!-- views/HelloView.vue -->
	<template>
	</template>

	<script>
	export default {
		name: "HelloView",
	}
	</script>
	```

2. route 추가
	```js
	// router/index.js
	import HelloView from "@/views/HelloView"

	const routes = [
		...,
		{
			path: "/hello/:userName",
			name: "hello",
			component: HelloView
		},
	]
	```
#
#### lazy-loading
- 당장 사용하지 않을 컴포넌트는 나중에 로드하는 방식
```js
// router/index.js

const routes = [
	{
		path: "/about",
		name: "about",
		component: () => {
			import("@/views/AboutView"),
		}
	}
]
```

#
## Navigation Guard
- Vue router를 통해 URL에 접근할 때 다른 url로 redirect를 하거나 해당 URL로의 접근을 막는 방법
ex) 사용자의 인증 정보가 없으면 특정 페이지에 접근하지 못하게 함
#
- **네비게이션 가드의 종류**
	- 전역 가드: 애플리케이션 전역에서 동작
		- 다른 url 주소로 이동할 때 항상 실행
		- router/index.js에서 `router.beforeEach()`를 사용하여 설정
		- 콜백 함수의 값으로 3개의 인자를 받음
			- `to`: 이동할 URL 정보가 담긴 Route 객체
			- `from`: 현재 URL 정보가 담긴 Route 객체
			- `next`: 지정한 URL로 이동하기 위해 호출하는 함수, 콜백 함수 내에서 한 번만 호출 가능
		- URL이 변경되어 화면이 전환되기 전 `router.beforeEach()`가 호출됨
		- 화면이 전환되지 않고 대기 상태에서 `next()`가 호출되면 라우팅이 일어남
	#			
	- 라우터 가드: 특정 URL에서만 동작
		- `beforeEnter()`
			- route에 진입했을 때 실행됨
			- 라우터를 등록한 위치에 추가
			- 매개변수, 쿼리 등 값이 변경될 때는 실행되지 않고 다른 경로에서 탐색할 때만 실행됨
			- 콜백 함수는 `to`, `from`, `next`를 인자로 받음
	#
	- 컴포넌트 가드: 라우터 컴포넌트 안에 정의
		- `beforeRouteUpdate()`
			- 해당 컴포넌트를 렌더링하는 경로가 변경될 때 실행

#### 특정 리소스를 찾을 수 없는 경우(존재하지 않는 URL)
- routes의 최하단부에 `path: "*"` 형태로 /404에 redirect를 시켜줌
- catch를 이용해서 응답하는 중 오류가 생기면 404로 이동
	```js
	.catch((error) => {
		this.$router.push("/404")
	})
	```