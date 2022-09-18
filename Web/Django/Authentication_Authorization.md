# Django authentication system

- Django에서 제공하는 인증시스템
- `django.contrib.auth`
  - settings.py에 기본적으로 포함
- **Authentication**

  - 신원 확인

- **Authorization**
  - 권한 부여

## 인증 시스템 활용

**1. accounts라는 이름의 앱 생성 및 등록**

- 나중의 추가 설정을 위해서는 accounts라는 이름으로 통일하는 것이 좋음

#

**2. Custom User Model 사용하기**

- _User Model_: 프로젝트에서 user를 나타낼 때 사용하는 모델
- Django에서는 새 프로젝트에서 기본적인 User Model로 충분하더라도 Custom User Model을 설정하는 것을 권장(Highly recommended)
- 기본 User Model과 동일하게 작동하면서도 필요시 맞춤설정까지 가능하기 때문에
- 첫 migration 전에 할당 값으로 적용
- 기본 값 `auth.User`로 할당 돼 있는 것을 커스텀 모델로 재 할당
- 기본 값 내용은 settings.py의 부모 파일인 global_settings.py에 있음

  #

  **2-1. User 모델 대체**

  - 기존의 User 클래스를 override 하기 위해 AbstractUser를 상속받는 User 클래스 작성

  ```python
  # accounts/models.py
  from django.contrib.auth.models import AbstractUser

  class User(AbstractUser):
  	...
  ```

  #

  **2-2. 생성한 User 모델을 할당**

  ```python
  # settings.py

  AUTH_USER_MODEL = 'accounts.User'
  ```

  #

  **2-3. admin.py에 User 모델을 등록**

  - 기본 User 모델이 아니기 때문에 등록하지 않으면 admin site에 출력되지 않음

  ```python
  # accounts/admin.py

  from django.contrib import adimn
  from django.contrib.auth.admin import UserAdmin
  from .models import User

  admin.site.register(User, UserAdmin)
  ```

#

## Django Session

- Django는 _database-backed sessions_ 저장 방식을 기본 값으로 사용
- session 정보를 Django DB의 django_session 테이블에 저장
- 설정을 통해 다른 저장방식으로 변경 가능
- Django는 form에서처럼 session도 많은 부분을 고려하지 않아도 되게끔 도움을 줌

#

## 로그인 기능 만들기

### Login

- 로그인은 Session을 만드는(Create) 과정
- `AutenticationForm`이라는 form을 사용

```python
# accounts/urls.py

from django.urls import path
from . import views

app_name = "accounts"
urlpatterns = [
  path("login/", views.login, name="login"),
]
```

```python
# accounts/views.py
from django.contrib.auth.forms import AutenticationForm
# 내가 정의한 login 함수와 이름이 겹치지않게 auth_login으로 지정
# 로그인 하고자하는 사용자 정보를 입력 받음
# 기본적으로 username과 password가 유효한지 검증
# request를 첫번째 인자로 받음
from django.contrib.auth import login as auth_login

def login(request):
  if request.method == "POST":
    authentication_form = AuthenticationForm(request, request.POST)
    if authentication_form.is_valid():
      auth_login(request, authentication_form.get_user())
      return redirect("articles:index")

  else:
    # render를 위한 form 출력
    authentication_form = AuthenticationForm()
  context = {
    "authentication_form": authentication_form,
  }
  return render(request, "accounts/login.html", context)
```

```html
<!-- accounts/login.html -->
{% extends "base.html" %} {% block content %}

<h1>로그인</h1>
<!-- 로그인 데이터로 로그인 요청을 보내기 위한 코드 -->
<form action="{% url 'accounts:login' %}" method="POST">
  {% csrf_token %} {{ form.as_p }}
  <input type="submit" />
</form>
{% endblock content %}
```

```html
<!-- base.html -->
...
<h1>Hello</h1>
<!-- 단순이 로그인 페이지로 가기위한 코드(render) -->
<a href="{% url 'accounts:login' %}">Login</a>
...
```

#

### 로그인 돼 있는 유저 정보

- `{{ user }}`를 통해 출력 가능
- 어떻게 context로 넘겨주는 과정 없이 바로 user를 쓸 수 있을까?
  - *settings.py*의 context processors 설정 값 때문에 template에 기본 적으로 변수가 포함됨
- `django.contrib.auth.context_processors.auth`에 포함
- 로그인하지 않은 경우에는 `AnonymousUser`로 출력

#

### Logout

- 로그아웃은 Session을 삭제(Delete)하는 과정

```python
# accounts/urls.py

from django.urls import path
from . import views

app_name = "accounts"
urlpatterns = [
  path("login/", views.login, name="login"),
  path("login/", views.logout, name="logout"),
]
```

```python
# accounts/views.py
# 내가 정의한 login 함수와 이름이 겹치지않게 auth_login으로 지정
# 로그인 하고자하는 사용자 정보를 입력 받음
# 기본적으로 username과 password가 유효한지 검증
# request를 첫번째 인자로 받음
from django.contrib.auth import logout as auth_logout

def logout(request):
  auth_logout(request)
  return redirect("article:index")
```

```html
<!-- base.html -->
...
<h1>Hello</h1>
<form action="{% url 'accounts:logout' %}" method="POST">
  {% csrf_token %}
  <input type="submit" value="Logout" />
</form>
...
```

#

### Sign Up

- User를 만드는(Create) 것
- `UserCreationForm`라는 ModelForm을 사용
  - 3개의 필드를 가짐
    - 1. `username` User Model에서 상속
    - 2. `password1` widget
    - 3. `password2` widget

```python
# accounts.py

app_name = "accounts"
urlpatterns = [
  ...,
  path("signup/", views.signup, name="signup"),
]
```

```python
# accounts/views.py
from django.contrib.auth.forms import AuthenticationForm, #UserCreationForm
from .forms import CustomUserCreationForm, CustomUserChangeForm

def signup(request):
  if request.method == "POST":
    # user_creation_form = UserCreationForm(request.POST)
    user_creation_form = CustomUserCreationForm(request.POST)
    if user_creation_form.is_valid():
      # 회원가입 후 바로 로그인 시키기
      # user_creation_form.save()
      new_user = user_creation_form.save()
      auth_login(request, new_user)
      return redirect("articles:index")
  else:
    # user_creation_form = UserCreationForm()
    user_creation_form = CustomUserCreationForm()
  context = {
    "user_creation_form": user_creation_form,
  }
  return render(request, "accounts/signup.html", context)
```

UserCreationForm은 커스텀 User 모델을 사용하는 것이 아닌 기본으로 제공되는 User 모델을 사용하기 때문에 상속 받는 모델을 수정해줘야함

- 커스텀 User 모델을 사용하려면 다시 작성하거나 확장해야하는 Form
  - `UserCreationForm`
  - `UserChangeForm`
- 기존 User 모델을 참조하지 않는 Form**(AbstractBaseUser의 모든 subclass와 호환됨)**
  - `AuthenticationForm`
  - `SetPasswordForm`
  - `PasswordChangeForm`
  - `AdminPasswordChangeForm`

```python
# accounts/forms.py

from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class CustomUserCreationForm(UserCreationForm):

  class Meta(UserCreationForm.Meta):
    model = get_user_model()

class CustomUserChangeForm(UserChangeForm):

  class Meta(UserChangeForm.Meta):
    model = get_user_model()
```

- `get_user_model()`
  - 현재 프로젝트에서 활성화된 사용자 모델(active user model)을 반환
  - model에 User클래스를 직접 참조하는 대신 `get_user_model`을 사용해서 참조하라고 명시

```html
<!-- signup.html -->
...
<!-- 회원가입 내용을 작성하고 요청을 보내기 위한 페이지 -->
<h1>회원가입</h1>
<form action="{% url 'accounts:signup' %}" method="POST">
  {% csrf_token %} {{ form.as_p }}
  <input type="submit" />
</form>
...
```

```html
<!-- base.html -->
...
<a href="{% url 'accounts:signup' %}">Sign Up</a>
...
```

#

### Delete

- 회원 탈퇴는 DB에서 User를 삭제하는 것

```python
# accounts/urls.py

app_name = "accounts"
urlpatterns = [
  ...,
  path("delete/", views.delete, name="delete"),
]
```

```python
# accounts/views.py

def delete(request):
  # 현재 로그인 돼 있는 유저를 삭제하기 때문에
  # 따로 어떤 유저인지 정보를 받을 필요가 없음
  request.user.delete()
  # 탈퇴하고 난 후에 로그아웃을 통해 유저의 세션정보도 삭제
  auth_logout(request)
  return redirect("articles:index")
```

```html
<!-- base.html -->

...,
<form action="{% url 'accounts:delete' %}" method="POST">
  {% csrf_token %}
  <input type="submit" value="회원탈퇴" />
</form>
```

#

### Update

- 회원정보 수정은 User의 내용을 Update 하는 것
- `UserChangeForm` 사용

```python
# accounts/urls.py

urlpatterns = [
  ...,
  path("update/", views.update, name="update"),
]
```

```python
# accounts/views.py

def update(request):
  if request.method == "POST":
    custom_user_change_form = CustomUserChangeForm(request.POST, instance=request.user)
    if custom_user_change_form.is_valid():
      custom_user_change_form.save()
      return redirect("articles:index")
  else:
    custom_user_change_form = CustomUserChangeForm(instance=request.user)
  context = {
    "custom_user_change_form": custom_user_change_form,
  }
  return render(request, "accounts/update.html", context)
```

```html
<!-- accounts/update.html -->

...
<h1>회원정보 수정</h1>
<form action="{% url 'accounts:update' %}" method="POST">
  {% csrf_token %} {{ form.as_p }}
  <input type="submit" />
</form>
```

```html
<!-- base.html -->
...
<a href="{% url 'accounts:update' %}">회원정보 수정 페이지</a>
```

현재 상태에서는 일반 유저가 변경하면 안 되는 정보까지 수정이 가능하기 때문에 커스텀 user 모델에서 modelForm으로부터 상속받는 내용을 수정해줘야함

```python
# accounts/forms.py

class CustomUserChangeForm(UserChangeForm):

  class Meta(UserChangeForm.Meta):
    model = get.user_model()
    # 상속받는 필드 명시
    # UserChangeForm의 기존 제공 필드명들은 github 공식문서에서 확인 가능
    fields = ("email", "first_name", "last_name")
```

#

### Change Password

- 이전 비밀번호를 입력하여 비밀번호 변경
- `SetPasswordForm`(이전 비밀번호를 입력하지 않고 비밀번호 변경)을 상속받아 사용

```python
# accounts/url.py

app_name = "accounts"
urlpatterns = [
  ...,
  path("password/", views.change_password, name="change_password"),
]
```

```python
# accounts/views.py
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm

def change_password(request):
  if request.method == "POST":
    password_change_form = PasswordChangeForm(request.uesr, request.POST)
    if password_change_form.is_valid():
      password_change_form.save()
      return redirect("articles:index")
  else:
    password_change_form = PasswordChangeForm(request.uesr)
  context = {
    "password_change_form": password_change_form,
  }
  return render(request, "accounts/change_password.html", context)
```

```html
<!-- accounts/change_password.html -->

...,
<form action="{% url 'accounts:change_password' %}" method="POST">
  {% csrf_token %} {{ form.as_p }}
  <input type="submit" />
</form>
```

### 로그인 사용자에 대해 접근 제한하기

1. `is_authenticated` attribute (the raw way)

- 권한(permission)과는 관련 없으며, 사용자의 상태나 세션에 대해서도 확인하지 않음
- User model의 속성
- 모든 User 인스턴스에 대해 항상 True인 읽기 전용 속성
- AnonymousUser에 대해서는 항상 False

```html
<!-- 로그인과 비로그인 상태에서 출력되는 화면 다르게 표시하기 -->
<!-- 하지만 비로그인 상태에서도 url를 직접 입력하면 로그인 사용자의 페이지로 갈 수 있음 -->
{% if request.user.is_authenticated %} ..., {% else %}
<a href="{% url `accounts:login` %}">Login</a>
<a href="{% url `accounts:signup` %}">Sign Up</a>
{% endif %}
```

2. `login_required` decorator

- 사용자가 로그인 되어 있으면 정상적으로 view 함수 실행
- 로그인 하지 않은 사용자의 경우 settings.py의 LOGIN_URL 문자열 주소로 redirect
  - LOGIN_URL의 기본 값은 "/accounts/login"
  - app의 이름을 accounts로 한 이유 중 하나
  - 인증 성공 시 redirect 되어야하는 경로는 "next"라는 쿼리 문자열 매개변수로 저장

```python
# accounts/views.py

from django.contrib.auth.decorators import login_required

@login_required
def something_needed_login(request):
  pass
```

- "next" 쿼리 문자열 매개변수를 처리하는 방법

```python
# accounts/views.py

def login(request):
...,
  return redirect(request.GET.get('next') or 'articles:index')
```

#### 두 데코레이터(@login_required, @require_POST)로 인해 발생하는 구조적인 문제

1. 비 로그인 상태로 게시글 삭제 시도
2. delete 함수의 @login_required로 인해 로그인 페이지로 redirect
   *http://127.0.0.1:8000/accounts/login/?next=/articles/1/delete/*
3. redirect로 이동한 로그인 페이지에서 로그인 진행
4. delete 함수의 @require_POST로 인해 에러 발생
   로그인 성공 이후 GET method로 next 파라미터 주소에 redirect되기 때문

#### 해결방안

- `@login_required`는 GET request method를 처리할 수 있는 view 함수에서만 사용해야함
- POST method만 허용하는 delete같은 함수는 내부에서 `is_authenticated` 속성 값을 사용해서 처리
