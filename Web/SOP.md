# SOP(Same-Origin Policy)
- 동일 출처 정책
	- Protocol, Host, Port까지가 출처
- 불러온 문서나 스크립트가 다른 출처의 리소스와 상호작용 하는 것을 제한하는 방식
- 해로울 수 있는 문서를 분리함으로써 공격 경로를 차단함
- 출처가 위배되는 경우 서버에서 응답을 하더라도 브라우저에서 거절

### CORS(Cross-Origin Resource Sharing) policy
- 교차 출처 리소스 공유 정책
- 추가 HTTP Header를 사용하여 다른 출처의 자원에 접근할 수 있는 권한을 허용하도록 브라우저에 알려주는 체제
	- 어떤 출처에서 자신의 컨텐츠와 상호작용 할 수 있는지 서버에 지정해주는 방법
- `Access-Control-Allow-Origin`, `Access-Control-Allow-Credentials`, `Access-Control-Allow-Headers`, `Access-Control-Allow-Methods`

#### Django cors headers Library
- `$ pip install django-cors-headers`
- `https://github.com/adamchainz/django-cors-headers`
- 응답에 CORS header를 추가해주는 라이브러리