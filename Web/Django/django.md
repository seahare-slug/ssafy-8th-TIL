# Django

- 서버를 구현해 주는 프레임워크
- 사용자의 요청에 따라 적절한 응답을 통해 동적 웹 페이지를 쉽게 만들 수 있게 해주는 프레임워크
- MTV 디자인 패턴 사용(MVC 패턴의 변형)

#

### 명령어

---

```
# 프로젝트 폴더 생성
$ django-admin startproject {project-name} .
# 서버 실행
$ python manage.py runserver
# 어플리케이션 생성
$ python manage.py startapp {어플리케이션 명(복수형으로 작명)}
```

```
어플리케이션 안에 "templates" 폴더 생성

- 실제 보여줄 web 파일
- 폴더 이름은 반드시 templates로 설정"
```

#

프로젝트 > _setting.py_

```python
# 어플리케이션 등록
# local apps -> third party apps -> django apps 순서로 추가
INSTALLED_APPS = [
	"어플리케이션명",
	...
]
```

어플리케이션 > _views.py_

```python
# view 안에 특정 화면을 렌더링할 함수를 생성
def index(request):
	return render(request, 'index.html')
```

프로젝트 > _urls.py_

```python
from {어플리케이션 명} import views
# url 추가와 해당 url 요청시 응답해줄 함수를 작성4
urlpatterns = [
	path('index/', views.index),
]
```

#

## 프로젝트 폴더 구성

- _\_\_init\_\_.py_

  - python에게 이 디렉토리를 하나의 python 패키지로 다루도록 지시

- _asgi.py_

  - Asynchronous Server Gateway Interface
  - 비동기식 웹 서버와 연결 및 소통하는 것을 도움

- _wsgi.py_

  - Web Server Gateway Interface
  - 웹서버와 연결 및 소통하는 것을 도움

- _settings.py_

  - 프로젝트 설정을 관리

- _urls.py_

  - 사이트의 url과 적절한 view의 연결을 지정

- _manage.py_
  - 프로젝트와 다양한 방법으로 상호작용하는 커맨드라인 유틸리티

#

## 어플리케이션 폴더 구성

- _admin.py_

  - 관리자용 페이지를 설정하는 곳

- _apps.py_

  - 앱의 정보가 작성되는 곳

- _models.py_

  - 어플리케이션에서 사용하는 Model을 정의하는 곳
  - MTV 패턴에서 "M"

- _test.py_

  - 프로젝트의 테스트 코드를 작성하는 곳

- _views.py_

  - view 함수들이 정의 되는 곳
  - MTV 패턴에서 "V"
