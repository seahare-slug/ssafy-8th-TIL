# Django URLs

## Variable routing

- url에 변수를 대입해서 url에 따라 다른 결과를 나오게 하고 싶을 때
- 기본 타입은 string이고 총 5개 타입이 존재 (str, int, slug, uuid, path)

```html
<!-- hello.html으로 접근할 수 있는 파일 -->

<!-- 이동 링크를 통해서 name 변수에 값을 전달 -->
<a href="{% url 'hello' name=instance.name %}">이동</a>
```

```python
# urls.py

# name이라는 이름으로 전달 받은 변수를 url에 참조하고 views.hello 함수의 인자로 전달
urlpatterns = [
	path('hello/<str:name>/', views.hello),
]
```

```python
# articles/views.py

# url 변수로 받은 인자를 받아서 template로 랜더링
def hello(request, name):
	context = {
		'name': name,
	}
	return render(request, 'hello.html', context)
```

```html
<!-- airtlcels/tempaltes/hello.html -->

<!-- hello 함수에서 랜더링할 html에 name을 전달받아 표시 -->
{% extends 'base.html' %} {% block content %}
<h1>안녕하세요 {{name}} 님</h1>
{% endblock %}
```

## App URL mapping

- 앱이 많아졌을 때 앱끼리 내부 views 파일 이름이나 함수가 겹칠 수 있음
- 각각의 앱 안에 urls.py를 만든 후 프로젝트의 urls.py에서 각 앱의 urls.py를 연결 해줌

```python
# include를 이용한 방법
from django.contrib import admin
#include 모듈을 가져와야함
from django.urls import path, include

urlpatterns = [
	# 기본적인 등록
	path('admin/', admin.site.urls),
	# 프로젝트의 urls에 articles의 urls를 포함
	path('articles/', include('articles.urls')),
	# 프로젝트의 urls에 pages의 urls를 포함
	path('pages/', include('pages.urls')),
	# 포함시키려는 앱의 urls.py에 urlpatterns가 빈 리스트라도 선언 되어 있어야함
]
```

## Naming URL patterns

- 주소 자체를 변수를 사용해서 관리하는 방법
- _index/_ 주소를 여러곳에서 상위 디렉토리로 사용하는 도중 *new-index/*로 주소명을 바꿔야한다면, 주소를 사용한 모든 곳을 찾아서 변경해야 함
- URL을 직접 사용하는 것이 아닌 path를 선언할 때 name 인자를 이용하여 저장

```python
# articles/urls.py

urlpatterns = [
	# "index/"라는 url이 name="index"에 저장이 돼서 url을 new_index/로 바꾸어도 다른 곳에는 name의 index로 저장이 돼 있어서 모두 같이 변함
	path('index/', views.index, name='index'),
	path('throw/', views.throw, name='throw'),
	path('hello/<str:name>/', views.hello, name='hello'),
]
```

- Built-in tag "url"
- 주어진 urlpatterns의 이름 또는 선택적 매개변수의 절대 경로 주소를 반환

```html
<!-- name='hello'에 해당하는 urlpatterns의 절대경로를 반환 -->
{% url 'hello' %}
```

#

# Q n A

> Q. urlpatterns 에 등록된 경로 말고 원래 파일 구성에 따른 경로 접근은 왜 안 되는지?
> A. 설계된 로직대로 접근할 수 있도록 urlpatterns 에 등록 돼 있지 않은 경로는 접근하지 못하게 Django에서 막어놓음
