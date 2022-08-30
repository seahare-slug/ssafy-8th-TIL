# Django

- 서버를 구현해 주는 프레임워크
- 사용자의 요청에 따라 적절한 응답을 통해 동적 웹 페이지를 쉽게 만들 수 있게 해주는 프레임워크
- MTV 디자인 패턴 사용(MVC 패턴의 변형)

## 명령어

```
# 프로젝트 폴더 생성
$ django-admin startproject {project-name} .
# 서버 실행
$ python manage.py runserver
# 어플리케이션 생성
$ python manage.py startapp {어플리케이션 명(복수형으로 작명)}
```

## 프로젝트 폴더 구성

- \_\_init\_\_.py

  - python에게 이 디렉토리를 하나의 python 패키지로 다루도록 지시

- asgi.py

  - Asynchronous Server Gateway Interface
  - 비동기식 웹 서버와 연결 및 소통하는 것을 도움

- wsgi.py

  - Web Server Gateway Interface
  - 웹서버와 연결 및 소통하는 것을 도움

- settings.py

  - 프로젝트 설정을 관리

- urls.py

  - 사이트의 url과 적절한 view의 연결을 지정

- manage.py
  - 프로젝트와 다양한 방법으로 상호작용하는 커맨드라인 유틸리티

## 어플리케이션 폴더 구성
