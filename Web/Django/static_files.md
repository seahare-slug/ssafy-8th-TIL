# Static Files(정적 파일)

- 응답할 때 파일의 내용 그대로 보여주는 파일
- 사용자의 요청에 따라 내용이 바뀌는 것이 아닌 파일
- 웹사이트에서 일반적으로 이미지, JS, CSS 등과 같은 미리 서버에 탑재되어 준비된 파일들과 사용자가 웹에 업로드 하는 파일들이 될 수 있음

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

### 사용자의 정적 파일 업로드 관리

- `ImageField()` 모델 필드를 이용하여 이미지 업로드 관리
- `FileField()` 모델 필드를 이용하여 파일 업로드 관리

1. settings.py에 `MEDIA_ROOT`, `MEDIA_URL` 설정

- `MEDIA_ROOT` -사용자가 업로드 한 파일을 보관할 절대 경로
  - Django는 성능을 위해 업로드 파일은 DB에 저장하지 않음
  - `MEDIA_ROOT`는 `STATIC_ROOT`와 다른 경로여야 함
  - `MEDIA_URL` -`MEDIA_ROOT`에서 제공되는 미디어 파일을 처리하는 URL
    - 업로드된 파일의 주소(URL)를 만들어주는 역할
    - 마찬가지로 `STATIC_URL`과 달라야함
