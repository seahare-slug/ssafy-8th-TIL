# Static Files(정적 파일)

- 응답할 때 파일의 내용 그대로 보여주는 파일
- 사용자의 요청에 따라 내용이 바뀌는 것이 아닌 파일
- 웹사이트에서 일반적으로 이미지, JS, CSS 등과 같은 미리 서버에 탑재되어 준비된 파일들과 사용자가 웹에 업로드 하는 파일들이 될 수 있음

#

### Django에서 정적 파일을 사용하기 위한 단계

1. INSTALLED_APPS 에서 `django.contrib.staticfiles` 포함
2. settings.py에서 `STATIC_URL` 정의
3. apps의 static 폴더에 정적 파일들 위치시키기
4. 사용할 templates에서 `static` 태그를 이용하여 지정된 경로에 있는 정적 파일의 URL 연결

   ```html
   <!-- index.html -->
   {% load static %}

   <img src="{% static 'some_static.files' %}" alt="something" />
   ```

#

- **`STATIC_ROOT`**

  - 실제 서비스 배포 환경에서는 다른 웹서버에 의해 실행되기 때문에 django의 정적 파일들을 인식하지 못함.
  - 내장되어 있는 정적 파일들을 밖으로 꺼내야 하는데 이러한 파일들을 모아두는 경로

  ```python
  # settings.py
  # 제일 바깥 위치에 staticfiles 폴더의 admin안에 정적파일들을 저장
  STATIC_ROOT = BASE_DIR / 'staticfiles'
  ```

  ```bash
  결과를 확인하고 수집된 정적파일을 모두 삭제

  $ python manage.py collectstatic
  ```

#

- **`STATICFILES_DIRS`**

  - apps/static/ 경로 이외에 추가적인 정적 파일 경로를 정의하는 리스트
  - 전체 경로를 포함하는 문자열로 작성되어야 함

  ```python
  # settings.py

  STATICFIELS_DIRS = [
  	BASE_DIR / 'static' ,
  ]
  ```

  ```html
  <!-- articles/index.html -->
  <!-- 기존 경로(apps/static/)의 파일 불러오기 -->
  {% load static %}

  <img src="{% static 'articles/somgthing.files' %}" alt="something1" />

  <!-- STATICFILES_DIR에 정의된 추가 경로(/static/)의 파일 불러오기 -->
  <img src="{% static 'somgthing.files' %}" alt="something2" />
  ```

#

- **`STATIC_URL`**

  - `STATIC_ROOT`에 있는 정적파일을 참조할 때 사용할 URL
  - 개발 단계에서는 실제 정적 파일들이 저장되어 있는 apps/static/ 경로와 STATICFILES_DIRS에 정의된 추가 경로들을 탐색

  ```python
  # settings.py

  STATIC_URL = '/static/'
  ```

#

### 사용자의 정적 파일 업로드 관리

- `ImageField()` 모델 필드를 이용하여 이미지 업로드 관리
- `FileField()` 모델 필드를 이용하여 파일 업로드 관리

#

**1. settings.py에 `MEDIA_ROOT`, `MEDIA_URL` 설정**

- `MEDIA_ROOT` -사용자가 업로드 한 파일을 보관할 절대 경로
  - Django는 성능을 위해 업로드 파일은 DB에 저장하지 않음
  - `MEDIA_ROOT`는 `STATIC_ROOT`와 다른 경로여야 함
  - `MEDIA_URL` -`MEDIA_ROOT`에서 제공되는 미디어 파일을 처리하는 URL
    - 업로드된 파일의 주소(URL)를 만들어주는 역할
    - 마찬가지로 `STATIC_URL`과 달라야함

#

**2. 사용자의 미디어 파일 업로드**

- Pillow 라이브러리 필요 (`$ pip install Pillow`)
- 같은 이름의 파일을 업로드하면 파일 이름 끝에 임의의 난수를 붙여서 저장

```python
# pjt1/urls.py

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
  ...,
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

- 업로드된 파일의 URL => `settings.MEDIA_URL`
- 위 URL을 통해 참조하는 실제 파일의 위치 => `settings.MEDIA_ROOT`

```python
# articles/models.py
# 이미지 입력받는 form 구성하기
  # blank 옵션은 필드를 비워둘 수 있음(DB에는 빈 문자열이 저장됨)
  # null 옵션도 있지만 문자열 기반 필드는 NULL 보다는 빈 문자열을 권장
  # upload_to 속성을 통해서 새로운 이미지 경로 추가 가능(MEDIA_ROOT 이후로 경로 추가)
  # 1. 문자열 값이나 경로로 지정
class Articles(models.Model):
  ...
  image = models.ImageField(blank=True, upload_to="something/" )
  ...

  # 2. 함수로 호출하는 방법
  # 해당하는 함수는 반드시 인자 2개를 가짐
  # `instance`: FileField가 정의된 모델 인스턴스
  # `filename`: 기존 파일 이름
def articles_image_path(instance, filename):
  return f"images/{instance.user.username}/{filename}"

class Articles(models.Model):
  ...
  image = models.ImageField(blank=True, upload_to=articles_image_path)
  ...
```

```html
<!-- articles/create.html -->
<!-- 파일 또는 이미지 입력받는 창 표시해주기 -->
...
<!-- 파일 또는 이미지 업로드 시에는 form 태그에 enctype 속성을 아래처럼 할당 -->
<form
  action="{ url 'articles:create' %}"
  method="POST"
  enctype="multipart/form-data"
>
  {% csrf_token %} ...
</form>
```

```python
# articles/views.py
# 파일 및 이미지는 request.POST로 넘길 수 없고 request.FILES 속성으로 넘겨주어야 함
def create(request):
  if request.method == "POST":
    form = ArticleForm(request.POST, request.FILES)
```

#

**3. 사용자가 업로드한 미디어 파일 표시하기**

- 업로드된 파일의 상대적 URL은 Django가 제공하는 url 속성을 통해 얻을 수 있음

```html
<!-- articles/detail.html -->

...
<!-- 이미지 데이터가 있는 경우에만 출력 -->
<!-- 그렇지 않으면 이미지가 없는 경우에 페이지 자체가 오류가 뜸 -->
{% if article.image %}
<img src="{{ article.image.url }}" alt="{{ article.image }}" />
{% endif %} ...
```

- `article.image.url`: 업로드된 파일의 경로
- `aritcle.image`: 업로드된 파일의 이름

#

### Image resizing

- 실제 원본 이미지를 그대로 서버에 올리면 부담이 큼
- HTML의 `<img>`태그로 직접 사이즈를 정해 놓을 수도 있지만, 업로드 될 때 이미지 자체를 resizing 하는 의미에서 조금 다름

**django-imagekit 모듈 설치 및 등록**

```
$ pip install django-imagekit
```

```python
# settings.py

ISTALLED_APPS = [
  ...,
  "imagekit",
]
```

**1. 원본이미지를 저장하지 않는 경우**

```python
# apps/models.py

from imagekit.processors import Thumbnail
from imagekit.models import ProcessedImageField

# ProcessedImageField는 내부 속성이 바뀌더라도 makemigrations 없이 바로 반영됨
class Model_Name(models.Model):
  ...,
  image = ProcessedImageField(
    blank=True,
    upload_to="thumbnails/",
    processors=[Thumbnail(200,300)],
    format="JPEG",
    options={"quality": 80},
  )
```

**2. 원본이미지를 저장하는 경우**

- 처음에는 기본 이미지로 사용하다가 썸네일(resizing image)을 사용하면 그때 생성

```python
# apps/models.py

from imagekit.processors import Thumbnail
from imagekit.models import ProcessedImageField, ImageSpecField

# ProcessedImageField는 내부 속성이 바뀌더라도 makemigrations 없이 바로 반영됨
class Model_Name(models.Model):
  ...,
  image = models.ImageField(blank=True)
  image_thumbnail = ProcessedImageField(
    blank=True,
    upload_to="thumbnails/",
    processors=[Thumbnail(200,300)],
    format="JPEG",
    options={"quality": 80},
  )
```
