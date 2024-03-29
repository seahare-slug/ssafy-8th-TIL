## Vue 의 기본 형태

### `el(element)`
- Vue instance와 DOM을 연결(mount)하는 옵션

- Vue instance와 연결되지 않은 DOM 외부는 Vue의 영향을 받지 않음


### `data`
- Vue instance의 데이터 객체 혹은 인스턴스 속성
- 데이터 객체는 반드시 기본 객체여야함(`{}`)
- 객체 내부의 아이템들은 value로 모든 타입의 객체를 가질 수 있음
- 정의된 속성은 interpolation `{{}}`을 통해서 view에 렌더링이 가능함

### `methods`
- Vue instance의 method들을 정의하는 곳
- Arrow Function은 this가 상위 스코프를 가리키기는 문제 때문에 사용하지 않는 걸로(호출은 가능할지 몰라도 현재 객체의 data를 변경하지 못함)
- this를 사용하여 객체 내의 data 변경 가능
- DOM에 바로 변경된 결과를 반영
	- Vue의 강력한 반응성(reactivity)

### `computed`
- method와 기본적인 구성은 비슷하지만 한 번 실행된 값을 저장해놓기 때문에 변화가 없다면 호출을 다시 하지 않고 계산된 값만 다시 보내줌
- 계산된 값이기 때문에 사용할 때 `()`를 붙이지 않음
- 참조하는 값이 변하면 다시 호출되어 재계산함(메서드는 상관없이 그냥 사용할 때마다 호출됨)


### `watch`
- 특정 데이터의 변화를 감지하는 기능
	1. watch 객체를 정의
	2. 감시할 대상 data를 지정
	3. data가 변할 시 실행 할 함수를 정의
		- 첫 번째 인자는 변동 전 data, 두 번째 인자는 변동 후 data
```html
<button @click="number++"></button>

<script>
	const app = new Vue({
		data: {
		number: 0,
		},
		watch: {
			number: function (val, oldVal) {
				console.log(val, oldVal)
			},
		}
	})
</script>
```
+)
- 실행함수를 Vue method로 대체 가능
	1. 감시 대상 data의 이름으로 객체 생성
	2. 실행하고자 하는 method를 handler에 문자열 형태로 할당
- Array, Object의 내부 요소 변경을 감지하기 위해서는 `deep`속성 추가 필요

### `filters`
- 텍스트 형식화를 할 수 있는 필터
- `interpolation`이나 `v-bind`를 이용할 때 적용 가능
- 표현식 마지막에 `|`와 함께 추가하여 사용
- chaining 사용 가능


### Template Interpolation
- 가장 기본적인 바인딩 방법
- 중괄호 2개 표기, DTL과 동일한 형태의 표기 (`{{}}`)
- JavaScript 식도 사용 가능