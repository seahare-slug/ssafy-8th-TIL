# Web app
- 웹 페이지가 그대로 보이는 것이 아닌 디바이스에 설치된 App 처럼 보이게 하는 것
- 웹 페이지가 디바이스에 맞는 적절한 UI/UX로 표현 되는 형태

## SPA(Single Page Application)
- 서버에서 최소 1개의 HTML만 전달받아 모든 요청에 대응하는 방식
- 이러한 대응이 가능한 이유는 **CSR(Client Side Rendering) 덕분**
	- CSR
		- 최초의 HTML 문서 하나를 받고 이후에 필요한 페이지의 데이터는 서버에 AJAX로 요청
		- 이러한 데이터를 JSON 형태로 받아와 JavaScript로 DOM트리에 반영(렌더링)
	- SSR
		- server가 사용자의 요청에 적합한 문서를 제공
		- 전달 받은 새 문서를 보여주기 위해 브라우저는 새로고침을 진행

#### CSR 방식의 장단점
- 장점
	- 트래픽 감소
		- 모든 페이지를 HTML로 받는 것이 아니기 때문에 트래픽이 감소하고 응답 속도가 빨라진다.
	
	- UX 향상
		- 매번 새로고침 되는 것이 아닌 필요한 부분만 고쳐짐

	- 협업이 용이
		- BackEnd와 FrontEnd 작업 영역을 명확하게 분리
	
- 단점
	- 첫 구동 시 필요한 데이터가 많으면 시작 시간까지 오랜 시간 소요

	- SEO(Search Engine Optimization)에 불리함
		- 첫 화면(메인 페이지)가 보통 비어있는 HTML
		- JS가 실행되고 난 뒤에는 seo가 확인하는 과정이 없음

#### CSR vs SSR
- 각 구동 방식은 서로 대립되는 것이 아님
	- 서비스마다 적합한 렌더링 방식이 존재함

- SPA 서비스지만 SSR 방식을 지원하는 Framework도 발전하고 있음
	- Vue의 Nuxt.js
	- React의 Next.js
	- Angular universal
	