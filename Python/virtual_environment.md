# Why are we use Virtual Environment

- 프로젝트마다 요구하는 버전이 다르지만 사용 가능한 서버는 하나일 때
- 각 프로젝트마다 필요한 라이브러리 버전을 맞게 관리하기 위해

### Set up venv

python 3.3 버전 이상부터 가능(command prompt)

```python
# 가상환경 생성(프로젝트 폴더와 동등한 위치)
$ python -m venv {가상환경 폴더 이름}
# 가상환경 실행
$ {가상환경 폴더 이름}\Scripts\acivate
# 가상환경이 실행 됐을 때 cli 표시
(가상환경 폴더 이름) $
# 실행 시킨 상태에서 원하는 라이브러리들 다운
(가상환경 폴더 이름) $ pip install Django3.0
(가상환경 폴더 이름) $ pip install -r requirement.txt
# 가상환경 종료
(가상환경 폴더 이름) $ deactivate
```

```python
# 현재 라이브러리를 txt로 변환할 때
$ pip freeze > requirements.txt
```
