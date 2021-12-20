# Musinsa Macros

무신사 웹페이지 및 앱 매크로입니다.

## 주의

코드가 있는 폴더에 ChromeDriver가 있어야 함

[링크](https://chromedriver.chromium.org/downloads)에서 자신의 크롬 버전에 맞는 드라이버 설치

## web.py 사용법

purchase_time 변수에 구입을 원하는 시간을 저장(서버시간을 기준으로 실행됨)

url에 구입하고자 하는 상품의 링크를 저장

[링크](https://www.whatismybrowser.com/detect/what-is-my-user-agent)에 접속해 User Agent를 복사한 후 user_agent 변수에 저장

options에 사이즈를 저장(옵션 선택이 없을 경우 빈 배열)

이후 실행시 무신사 홈페이지에 로그인 한 후 기다리면 자동으로 구입 진행

## app.py 사용법

안드로이드 에뮬레이터를 이용해 무신사 설치 후 로그인

구매하고자 하는 상품을 좋아요 1번에 등록

이후 DEBUG를 True로 바꾼 후 실행하여 변수들의 좌표를 자신의 컴퓨터에 맞게 저장

purchase 함수의 버튼이 활성화 됐을 때 좌표의 평균값을 자신의 컴퓨터에 맞게 저장

DEBUG를 False로 변경

구입할 시간을 입력한 후 좋아요 페이지에서 기다리면 자동으로 구입 진행
