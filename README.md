# Maple-Screenshot-Move
메이플스토리는 스크린샷 저장 경로 옵션을 게임 폴더 안, 바탕화면, C드라이브 이렇게 3가지밖에 제공하지 않습니다. 
이 파이썬 코드를 이용하면 원하는 경로로 저장된 스크린샷을 옮길 수 있습니다.

## 사용방법
1. [파이썬 설치](https://www.python.org/)
1. main.py를 원하는 경로에 다운받기
1. maplePath의 값을 메이플 설치 경로로 변경 (기본값 : C:/Nexon/Maple/)
1. screenshotPath의 값을 스크린샷을 옮길 경로로 변경 (기본값 : maplePath + "screenshot/", 기본값을 그대로 사용하실 경우 메이플 폴더 안에 screenshot 폴더를 만들어주세요)
1. **작업 스케줄러** 설정

### 작업 스케줄러 설정 방법
1. 작업 스케줄러 열기
1. 작업 만들기
1. 이름 설정
1. 동작탭 - 새로 만들기
1. **프로그램/스크립트**에 파이썬 설치 경로 (윈도우 기본 설치경로 : C:\User\\**사용자 이름**\AppData\Local\Programs\Python\Python**버전**\python.exe)
1. **인수 추가**에 main.py 경로
1. 트리거탭 - 원하는 실행 주기 설정 (ex: PC 켜질때마다 실행, 매일 저녁 8시 실행 등등)
 
자세한 설명은 [여기](https://blog.apteryx.moe/posts-1770/)를 참고하세요
