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
