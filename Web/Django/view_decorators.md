# Decorator

- 기존 작성된 함수에 특정 문법, 의미를 부여하거나 기능을 추가하고 싶을 때
- 요청 메서드(request.method)에 따라서 접근을 제한하고 싶을 때

  - django.views.decorators.http 데코레이터를 이용
    - `require_http_methods()`
    - `require_POST()`
    - `require_GET()`도 있지만 대신 `require_safe()`를 권장
    - `require_safe()`

#

```python
# views.py
from django.views.decorators.http import require_http_methods, require_POST

@require_http_methods(["GET", "POST"])
def create(requests):
	pass

@require_http_methods(["GET", "POST"])
def update(request, pk):
	pass

@require_POST
def delete(request, pk):
	article = Article.objects.get(pk=pk)
	...
```
