# CRUD 기본

- 모든 User 레코드 조회
  `User.objects.all()`

#

- User 레코드 생성
  ```
  User.objects.create(
  	attr="",
  	...
  )
  ```

#

- User의 101번 레코드의 last_name을 "김"으로 수정
  ```
  user101 = User.objects.get(pk=101)
  user101.last_name = "김"
  user.save()
  ```

#

- User의 101번 레코드 삭제
  ```
  user101 = User.objects.get(pk=101)
  user.delete()
  ```

#

- User 레코드 수 조회
  `User.objects.count()`
  `len(User.objects.all())`

#

- 중복없이 모든 지역 조회하기
  `User.objects.distinct().values("country")`

#

- User 레코드를 나이가 어린 순으로, 같은 나이면 계좌잔고가 많은 순으로 이름과 나이 조회하기
  `User.objects.order_by("age", "-balance").values("first_name", "age")`
- 역순 정렬은 `order_by`의 속성에 "-"하이픈을 넣으면 됨
  `User.objects.order_by("-age").values("first_name", "age")`

#

- 조회시 values 속성 사용 비교
  `User.objects.filter(age=30)`
  -> <QuerySet [object...]> 레코드의 모든 필드에 대한 key, value 반환
  `User.objects.filter(age=30).values("first_name")`
  -> <QuerySet [dict...]> 레코드의 지정된 필드에 대한 key, value만 반환

#

- 나이가 가장 어린 10명의 이름을 조회
  `User.objects.order_by("age").values("first_name")[:10]`

#

- `filter` 속성은 조회하고 싶은 필드 뒤에 언더바 두개와 옵션을 붙여 다양한 조건을 추가할 수 있음

  ```python
  # 포함여부
  filter(필드__contains="something")

  # 이상과 초과
  filter(필드1__gte=num1, 필드2__gt=num2)

  # 등등...
  ```

#

- `exclude` 속성은 입력된 인자와 일치하지 않은 객체를 반환
  경기도 혹은 강원도에 살지 않는 사람들의 이름 조회
  `User.objects.exclude(country__in=["경기도", "강원도"]).values("first_name")`

#

### Aggregation 활용

- 나이가 30살 이상인 사람들의 평균 나이 조회하기

```python
from django.db.models import Avg

User.objects.filter(age__gte=30).aggregate(avg_age=Avg("age"))
```

- 가장 높은 계좌 잔액 조회하기

```python
from django.db.models import Max

User.objects.aggregate(Max("balance"))
```

- 모든 계좌 잔액 총액 조회하기

```python
from django.db.models import Sum

User.objects.aggregate(Sum("balance"))
```

#

#### annotate()

- 쿼리의 각 항목에 대한 요약 값 계산
- SQL의 GROUP BY에 해당

#

- 각 지역별로 몇 명씩 살고 있는지 조회하기

```python
from django.db.models import Count

User.objects.values("country").annotate(number_of_people=Count("country"))
```

#

- 각 지역별 인원과 계좌 잔액 평균 한번에 계산하기
  `User.objects.values("country").annotate(Count("country"), Avg("balance"))`
