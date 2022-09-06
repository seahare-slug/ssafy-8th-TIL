# Django Form

- 우리가 여태까지 사용자로부터 데이터를 받을 때는 HTML의 form, input 태그를 통해서 받았음
- 이러한 방식은 서버로 들어오는 요청을 모두 수용하고 있기 때문에 보안상 위험함
- 그렇기 때문에 **유효성 검증**을 따로 고려해서 구현을 해주어야하는데
- **Django Form은 쉽게 유효성 검증을 할 수 있도록 만들어 줌**

1. 렌더링을 위한 데이터 준비 및 재구성
2. 데이터에 대한 HTML forms 생성
3. 클라이언트로부터 받은 데이터 수신 및 처리

### Form Class 선언 및 활용

```python
# 앱/forms.py
from django import forms

class FormName(forms.form):
	title = forms.CharField(max_length=10)
	content = forms.CharField()
```

- `forms.CharField()`: 입력에 대한 유효성 검사
- `forms.CharField(widget=forms.{weight-type})`: weight-type에 따라 다양한 요소를 렌더링 해줄 뿐이지 입력에 대한 **유효성 검사는 없음**

```python
# 앱/views.py
from .forms import FormName

def function1(request):
	form_name = FormName()
	context = {
		'form_name': form_name,
	}
	return render(request, "랜더링할 페이지", context)
```

```html
<!-- 앱/랜더링할 페이지 -->

<!-- p태그로 해당 form 인스턴스를 통해서 input, label까지 자동 생성 -->
{{ form_name.as_p }}
```

### ModelForm

- 기존에 Model Class에 필드에 대한 정보가 있는데 Form을 사용하기 위해 다시 같은 필드의 Class를 또 정의해줘야하는 것에 중복이 너무 많음
- 이러한 부분을 보완하기 위해 ModelForm을 활용

```python
# 앱/forms.py
from django import forms
# 이미 정의된 모델 Class를 가져옴
from .models import 모델명

class FormName(forms.ModelForm):

	class Meta:
		model = 모델명
		# 모델의 모든 필드 포함
		fields = "__all__"
		# 특정 칼럼 제외하고 나머지 모두 포함
		# exclude = ("title",)
		# 두가지 동시에 쓰이지는 않음
```

```python
# 앱/views.py
from .forms import FormName

def function1(request):
	# 사용자에게 받은 입력값
	form_name = FormName(request.POST)
	# ModelForm은 클래스 정의시 CharField를 사용하지 않고
	# 이미 있는 model을 전달 받아서
	# 입력값에 대해서 is_valid로 유효성 검사 필요
	if form_name.is_valid():
		form_instance = form_name.save()
		return redirect("성공시 이동할 url", form_instance.pk)
	return redirect("실패시 이동할 url")
```
