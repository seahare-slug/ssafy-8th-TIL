## Namespace

---

- 개체를 구분할 수 있는 범위를 나타내는 이름공간
- 서로 다른 앱 A, B 안에 같은 이름의 html 파일이 있을 때, routing이 돼 있는 경우에는 에러가 나지는 않지만 그 html 파일이 어느 앱의 파일인지 특정하지 못 함.
- 실행시 현재 앱의 html 파일로 이동
- 각 앱의 파일들을 특정 시켜주기 위해서 URL에 해당 앱의 이름을 추가시켜줌(app이름을 추가하여 유니크한 urlpattern을 생성)

```python
# apps1/urls.py

# app_name 이라는 속성을 통해서 URL에 앱 이름을 부여하여 고유한 urlpattern을 만듦
app_name = "apps1"
urlpatterns = [
    ...,
]
```

```python
# apps2/urls.py

app_name = "apps2"
urlpatterns = [
    ...,
]
```

## URL tag의 변화

- url 태그는 보통 _앱이름:urls.py에서 설정한 name_ 형태로 쓰지만 원한다면 일반 주소형태로 써도 무관함

```python
# apps1 앱의 URL name이 index인 urlpattern을 실행함
{% url 'index' %} ----> {% url 'apps1:index' %}
```

## Templatespace

---

- Django는 기본적으로 settings.py의 INSTALLED_APPS에 작성된 app 순서대로 template를 검색함
- url에 직접 주소를 입력시 **template를 기준**으로 일치하는지 보기 때문에 template의 **상위 경로가 달라도** 맞다고 판단
  > Q 원래 경로는 apps2/templates/index/인데 templates는 생략가능?
- 따라서 template 하위에 각 앱의 이름으로 폴더를 한번 더 생성 후 그 안에 html 파일들을 보관

```
apps1/templates/index.html ----> apps1/templates/apps1/index.html
```
