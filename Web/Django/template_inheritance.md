# 템플릿 상속

- 코드의 재사용에 중점
- 부모의 코드에 선언된 skeleton 코드 안의 {% block content %} 부분에 원하는 부분을 추가(override)하여 사용할 수 있음

```html
<!-- 최상단에 위치 -->
{% extends '{부모 템플릿}' %} {% block content %} {% endblock content %}
```

#

### 템플릿 경로 추가하기

- template 디렉토리를 다른 곳에 만들어 여러군데에서 재사용 하고 싶을 때
- 기본 template 경로가 아닌 다른 경로도 추가하여 그 부분의 template를 참조하여 사용

프로젝트 > _setting.py_

```python
TEMPLATE = [
	{
		...,
		"DIRS": [BASE_DIR / {원하는 경로}]
	}
]
```
