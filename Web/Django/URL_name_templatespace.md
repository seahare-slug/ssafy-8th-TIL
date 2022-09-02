## Namespace
---
- 개체를 구분할 수 있는 범위를 나타내는 이름공간
- 서로 다른 앱 A, B 안에 같은 이름의 html 파일이 있을 때, routing이 돼 있는 경우에는 에러가 나지는 않지만 그 html 파일이 어느 앱의 파일인지 특정하지 못 함. 
- 실행시 현재 앱의 html 파일로 이동
- 각 앱의 파일들을 특정 시켜주기 위해서 URL에 해당 앱의 이름을 추가시켜줌
```python
# apps1/urls.py

# app_name 이라는 속성을 통해서 URL에 앱 이름을 부여하여 고유한 URL을 부여
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
```
{% url 'index' %} ----> {% url 'apps1:index' %}
```

## Templatespace
---
- 