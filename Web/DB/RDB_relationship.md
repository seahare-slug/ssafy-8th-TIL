# RDB의 관계

- 테이블 간의 상호작용을 기반으로 설정되는 테이블 간의 논리적인 연결

> 예시
> ![example](./img/relationship_example.png)

- 외래 키(외부 키)

1. 1:1 관계

   - 한 테이블의 레코드 하나가 다른 테이블의 레코드 단 한 개와 관련된 경우
   - Django Relationship Field: `OneToOneField()`

2. N:1 관계

   - 한 테이블의 0개 이상의 레코드가 다른 테이블의 레코드 한 개와 관련된 경우
   - Django Relationship Field: [ForeignKey()](#foreignkeymodel_class-on_delete-options)
   - N:1 관계의 한계
     - 1의 입장에서 여러개의 N을 참고하고 싶을 때마다 새로운 객체를 계속 생성해주어야 함

3. M:N 관계

   - 한 테이블의 0개 이상의 레코드가 다른 테이블의 0개 이상의 레코드와 관련된 경우
   - 양쪽 모두에서 N:1 관계를 가짐
   - Django Relationship Field: [ManyToManyField](#manytomanyfieldmodel_class-options)

#

### ForeignKey(Model_Class, on_delete, \*\*options)

- N:1 관계를 담당하는 Django의 모델 필드 클래스
- 외래키에 해당하는 필드는 작성되는 위치와 관계없이 필드의 마지막에 작성됨
- 외래키의 인스턴스 이름은 참조하는 Model_Class 이름의 소문자 형태로 정의하는 것을 권장(칼럼의 이름이 참조하는 `모델이름_id` 형태로 작성되기 때문에 명시적인 이유)
- `on_delete`: 외래키가 참조하는 객체가 사라졌을 때 외래키를 가진 객체를 어떻게 처리할 지 정의

```python
# apps/models.py

class Comment(models.Model):
   article = models.ForeignKey(Article, on_delete=models.CASCADE)
   content = models.CharField(max_length=200)
   ...
```

- 이러한 외래키 필드를 통해 다른 모델의 값을 참조하여 사용하게 되면 향후 이것을 ModelForm으로 쓸 때 참조된 외래키의 값은 정해져 있어야 한다.
- 하지만 별다른 조치 없이 그대로 ModelForm으로 Template에 나타내게 되면 외래키에 해당하는 값도 사용자의 입력을 받게 된다.
- 따라서 exclude를 통해서 외래키에 해당하는 값은 제외 해 주어야 한다.

```python
# articles/forms.py

class CommentForm(forms.ModelForm):

   class Meta:
      model = Comment
      # Comment model의 article 필드는 외래키이기 때문에 제외하고 사용자의 입력을 받음
      exclude = ("article",)
```

- 여기서 제외된 외래키의 값은 url을 통해 넘기는 변수(pk값 등)로 view에 넘겨 외래키를 받아옴

```html
<!-- articles/detail.html -->

<form action="{% url 'articles:create' article.pk %}" method="POST">...</form>
```

```python
# articles/views.py

def create(request, pk):
   article = Article.objects.get(pk=pk)
   ...
```

- 그렇다면 위의 article 객체의 저장은 언제 이루어 질까?
- 위에서는 저장할 적절한 위치를 찾을 수 없음
- `save(commit=False)`를 이용해서 아직 DB에는 저장(commit)이 안 된 인스턴스를 반환

```python
# articles/views.py

def create(request, pk):
   article = Article.objects.get(pk=pk)
   ...
   if comment_form.is_valid():
      comment = comment_form.save(commit=False)
      comment.article = article
      comment.save()
   return ...
```

#

**Django에서 User모델 참조할 때**

- models.py에서 참조할 때는 `settings.AUTH_USER_MODEL` (정의하는 곳이기 때문)
- 다른 모든 곳에서는 `get_user_model()` (사용하는 곳이기 때문에 get)

```python
# apps/models.py

from django.conf import settings

class Article(models.Model):
   user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
   ...
```

#

- **역참조**
  - 나를 참조하는 테이블을 참조하는 것(본인을 외래키를 통해 참조 중인 테이블에 접근하는 것)
  - N:1에서 1이 N을 참조하는 상황

```python
# 논리상 Aritcle에는 Comment와 어떠한 관계도 정의 돼 있지 않아서 Article 객체가 Comment를 참조할 수 없지만 아래의 형태로 comment 객체를 참조 가능
# "모델명_set" 형태로 사용
# 이러한 역참조 시 사용하는 매니저(model_set) 이름은 `related_name` 옵션을 통해서 변경할 수도 있음
article.comment_set.method()
```

```shell_plus
# 1번 게시글 조회
article = Article.objects.get(pk=1)

# 1번 게시글에 작성된 모든 댓글 조회하기(역참조)
comments = article.comment_set.all()

# 1번 게시글에 작성된 모든 댓글 출력하기
for comment in comments:
   print(comment.content)
```

#

### ManyToManyField(Model_Class, \*\*options)

- 기존 N:1 관계의 한계를 극복하기 위해서는 중계 테이블을 이용해서 M:N 관계를 필요로하던 두 테이블을 연결 시켜줌

```python
# 의사와 환자의 M:N 관계

class Reservation(models.Model):
   doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
   patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
```

- 이러한 과정을 Django에서 `ManyToManyField`로 지원해줌

```python
# models.py

class Patient(models.Model):
   doctors = model.ManyToManyField(Doctor)
   name = models.TextField()
```

```python
# patient1이 doctor1에게 예약
patient1.doctors.add(doctor1)

# doctor1이 patient2를 예약
doctor1.patient_set.add(patient2)

# patient1이 예약한 의사 목록 확인
patient1.doctors.all()

# doctor1에게 예약된 환자 목록 확인
doctor1.patient_set.all()

# doctor1이 patient1의 예약 취소
doctor1.patient_set.remove(patient1)
```

- model_set 이름 말고 참조하는 이름을 설정해주고 싶으면 `related_name`사용
- 그 후로 기존의 model_set으로는 참조할 수 없음

```python
class Patient(models.Model):
   doctors = model.ManyToManyField(Doctor, related_name="patients")
   name = models.TextField()
```
