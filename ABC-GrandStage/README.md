# ABC Grand Stage 메크로

[ABC Grand Stage](https://grandstage.a-rt.com/?track=W0009) 사품을 자동으로 구입해 주는 매크로입니다.

## 사용법

코드가 있는 폴더에 [Chrome Driver](https://chromedriver.chromium.org/downloads) 설치

purchase_time 변수에 구입을 원하는 시간을 저장(서버시간을 기준으로 실행됨)

url에 구입하고자 하는 상품의 링크를 저장

[링크](https://www.whatismybrowser.com/detect/what-is-my-user-agent)에 접속해 User Agent를 복사한 후 user_agent 변수에 저장

size에 사이즈를 저장(옵션 선택이 없을 경우 빈 배열)

이후 실행시 홈페이지에서 로그인 한 후 기다리면 자동으로 구입 진행
