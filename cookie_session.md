# Cookie and Session

- HTTP에서 비연결 지향을 극복하고 서버와 클라이언트간의 상태 유지를 돕기 위한 도구

## Cookie

- 상태가 있는 세션을 만들도록 해 줌
- 사용자가 웹 사이트를 방문할 때 서버가 사용자의 웹 브라우저에 전송하는 작은 데이터 조각
- 브라우저는 이 조각을 로컬에 KEY-VALUE 형식으로 저장
- 나중에 동일한 서버에 재요청시마다 저장된 쿠키를 함께 전송하여 클라이언트의 정보 제공
- 주로 요청이 이전과 동일한 브라우저에서 왔는지 아닌지 판단할 때 사용됨

### Cookie Life Time

- **Session cookie** : 현재 세션이 종료되면 삭제, 브라우저 종료와 함께 삭제
- **Persistent cookies** : Expires / Max-age 속성에 지정된 기간이 지나면 삭제

## Session

- 사이트와 특정 브라우저 사이의 "state(상태)"를 유지시키는 것
- 클라이언트가 서버에 접속하면 서버가 session id를 발급, session id를 쿠키에 저장
- 서버는 쿠키 안의 session id를 통해 클라이언트의 상태를 식별

### 쿠키 사용 목적

**1. 세션 관리(Session management)**

- 로그인, 아이디 자동완성, 공지 하루 안보기, 장바구니

**2. 개인화(Personalization)**
**3. 트래킹(Tracking)**
