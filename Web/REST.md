# REST(Representational State Transfer)

- API server를 개발하기 위한 일종의 소프트웨어 설계 방법론
- 자원을 정의하고 자원에 대한 주소를 지정하는 전반적인 방법을 서술

**1. 자원을 식별 - URI**
**2. 자원에 대한 행위 - HTTP Methods**
**3. 자원을 표현 - JSON**

기존의 방식은 Django로 서버에서 사용자에게 원하는 HTML 파일을 바로 반환해주며 화면을 보여줬지만, 이제는 JSON 파일로 반환을 해주게 되면서 Django에서 화면을 보여주는 역할은 사라지게 된다. 즉, 프론트와 백엔드를 전부 Django가 담당하고 있었지만 이제는 백엔드만 담당하게 된다. 프론트엔드 부분은 나중에 Vue를 통해 다룰 예정이다.

아래의 내용은 Django에서 프론트에게 JSON(데이터)를 넘겨주는 상황에 대한 학습이다.

#

### 다양한 방법으로 서버에서 JSON를 응답해보기

**1. HTML 응답**

- 지금까지 해오던 html 응답 방식

```python
# apps/urls.py

urlpatterns = [
	path("html/", views.index),
]
```

```python
# apps/views.py

def index(request):
	...
	return render(request, "apps/index.html")
```

**2. JsonResponse()를 사용한 응답**

- Django에서 제공하는 JsonResponse 객체를 통해 python 데이터 타입을 JSON으로 변환하여 응답

**3. Django Serializer를 사용한 응답**
**4. Django REST framework를 사용한 응답**
