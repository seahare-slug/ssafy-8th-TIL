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

- Django에서 제공하는 `JsonResponse` 객체를 통해 python 데이터 타입을 JSON으로 변환하여 응답

```python
# apps/views.py

from django.http.response import JsonResponse

def index_json(request):
	articles = Article.objects.all()
	articles_json = []
	# 각 객체의 필드들을 일일이 json 형식으로 담아주어야함
	for article in articles:
		articles_json.append(
			{
				"id": article.pk,
				...,
			}
		)
	return JsonResponse(json_file)
```

**3. Django Serializer를 사용한 응답**

- Django에서 제공하는 `HttpResponse`를 활용하여 JSON으로 응답
- JSON의 모든 필드를 작성할 필요가 없음
- `seralization`: 직렬화, 데이터 구조나 객체 상태를 나중에 재구성 할 수 있도록 포맷하는 과정
- Django에서 `serialize`는 Queryset이나 Model instance와 같은 복잡한 데이터를 Python이 쉽게 변환할 수 있는 `JSON`이나 `XML`등으로 바꾸어 줌

```python
from django.http.response import HttpResponse
from djago.core import serializers

def index_json2(request):
	articles = Article.objects.all()
	data = serializers.serialize("json", articles)
	return HttpResponse(data, content_type="application/json")
```

**4. Django REST framework(DRF)를 사용한 응답**

- REST framework를 작성하기 위한 여러 기능을 제공
- DRF의 serializer는 Django의 Form, ModelForm 등과 매우 유사하게 작동

```python
# settings.py

INSTALLED_APPS = [
	...,
	"rest_framework",
]
```

```python
# apps/serializers.py

from rest_framework import serializers
from .models import ModelName

class ModelNameSerializer(serializers.ModelSerializer):
	class Meta:
		model = ModelName
		fields = "__all__"
```

```python
# apps/views.py

@api_view(["GET"])
def app_json_3(request):
	all_objects = ModelName.objects.all()
	# many 옵션은 여러개의 object를 serializer 할 때 필요
	serializer = ModelNameSerializer(all_objects, many=True)
	return Response(serializer.data)
```
