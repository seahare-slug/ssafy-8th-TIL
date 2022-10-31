# directive
- HTML의 기본속성이 아닌 Vue가 제공하는 특수 속성의 값으로 data를 작성
- `v-이름`의 형태로 값에는 JS 표현식을 작성할 수 있음
![form](./img/directive.PNG)
- 표현식의 값이 변경될 때 반응적으로 DOM에 적용하는 것이 역할
#

### Built-in directives
`v-text`
- template interpolation처럼 기본적인 바인딩 방법
- 1, 2의 결과는 같음
```html
<div id="app2">
	<!-- 1 -->
	<p v-text="message"></p>
	<!-- 2 -->
	<p>{{ message }}</p>
</div>

<script>
	const app2 = new Vue({
		el: "#app2",
		data: {
			message: "hello!",
		}
	})
</script>
```
#
`v-html`
- raw html을 표현할 수 있는 방법(html 문법을 그대로 표현)
- 사용자가 입력하는 부분에서는 사용 금지(XSS 공격 취약)
```html
<div id="app2">
	...
	<p v-html="some-html"></p>
</div>

<script>
	const app2 = new Vue({
		el: "#app2",
		data: {
			...,
			some-html: "<a href='#'>HI</a>"
		}
	})
</script>
```
#
`v-show`
- *Expensive initial load, cheap toggle*
- boolean 값이 변경될 때마다 반응
- 값에 따라 해당 element를 보여줄지 말지를 결정
- display 속성을 기본 값과 none으로 toggle
	- display 속성만 변경되었을 뿐 DOM에는 존재함
```html
<div id="app3">
	...
	<p v-show="isActive">보이니 안보이니?</p>
</div>

<script>
	const app3 = new Vue({
		el: "#app3",
		data: {
			isActive: false
		}
	})
</script>	
```
#
`v-if`
- *Cheap initial load, expensive toggle*
- `v-show`와 사용 방법은 동일
- 단, 값이 false인 경우 DOM에서 아예 사라짐
- 표현식 값이 자주 변경되지 않을 때 사용

#
`v-for`
- python처럼 `for .. in ..` 형식으로 작성
- 반복가능한 데이터 타입에 모두 사용 가능
- (data, index) 형태로 `enumerate`처럼 index도 접근 가능
- (key, value) 형태로 객체의 키와 값에 접근 가능
- 각 요소가 객체라면 `dot notation`으로도 접근 가능

```html
<div id="app1">
	<div v-for="(char, index) in myStr">
		<p>{{ index }}번째 문자 {{ char }}</p>
	</div>
</div>

<script>
	const app1 = new Vue({
		el: "#app1",
		data: {
			myStr: "hello"
		}
	})
</script>	
```